import ast
import copy
import runpy
import sys
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import MagicMock, patch
from uuid import uuid4

from fastapi.testclient import TestClient
from pymongo.errors import PyMongoError


def read_steps():
    steps = {}
    root = Path(__file__).resolve().parents[1] / "app" / "repositories"
    for path in root.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8-sig"))
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                continue
            documents = value if isinstance(value, list) else [value]
            for document in documents:
                if isinstance(document, dict) and "message" in document and "code" in document:
                    if document["code"] in steps:
                        raise ValueError("Código repetido: " + document["code"])
                    steps[document["code"]] = document
    return steps


class ChatbotTests(unittest.TestCase):
    def setUp(self):
        self.steps = read_steps()
        self.answers = {}
        self.database = ModuleType("app.database.database")
        self.database.db = MagicMock()
        self.database.db.step.find_one.side_effect = lambda query, projection: copy.deepcopy(self.steps.get(query["code"]))
        self.database.db.rating.update_one.side_effect = self.store_answer

        with patch.dict(sys.modules, {"app.database.database": self.database}):
            repository = runpy.run_path(str(Path(__file__).resolve().parents[1] / "app/repositories/chatbot.py"))
        chatbot = ModuleType("app.repositories.chatbot")
        chatbot.find_step = repository["find_step"]
        chatbot.save_answer = repository["save_answer"]
        self.find_step = chatbot.find_step

        service = ModuleType("app.repositories.service")
        service.find_available_services = MagicMock(return_value=[])
        service.find_support_title = MagicMock(return_value=[])
        service.find_services_descriptions = MagicMock(return_value=[])
        with patch.dict(sys.modules, {"app.repositories.chatbot": chatbot, "app.repositories.service": service}):
            module = runpy.run_path(str(Path(__file__).resolve().parents[1] / "app/routes/menu.py"))
        self.client = TestClient(module["app"])

    def store_answer(self, query, update, *, upsert):
        self.assertTrue(upsert)
        self.answers.setdefault(query["_id"], copy.deepcopy(update["$setOnInsert"]))

    def test_home_is_not_a_chatbot_option(self):
        for step in self.steps.values():
            for option in step.get("options", []):
                self.assertNotEqual(option.get("next step"), "MENU")
                self.assertNotIn(option["text"], ["Voltar para a tela inicial", "Voltar para a tela principal"])

    def test_all_destinations_exist(self):
        for step in self.steps.values():
            targets = [step.get("next step")]
            targets.extend(option.get("next step") for option in step.get("options", []))
            for target in targets:
                if target and target != "MENU":
                    self.assertIn(target, self.steps, (step["code"], target))

    def test_every_step_is_reachable(self):
        visited = set()
        pending = ["AM_1", "MI_01", "FB_01"]
        while pending:
            code = pending.pop()
            if code in visited:
                continue
            visited.add(code)
            step = self.steps[code]
            targets = [step.get("next step")]
            targets.extend(option.get("next step") for option in step.get("options", []))
            pending.extend(target for target in targets if target and target != "MENU")
        self.assertEqual(visited, set(self.steps))

    def test_steps_are_returned_without_object_ids(self):
        for code in self.steps:
            response = self.client.get("/steps/" + code)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["message"], self.steps[code]["message"])
            self.assertNotIn("_id", response.json())

    def test_legacy_codes(self):
        for old, new in {"AM_01": "AM_1", "MI_1": "MI_01", "AM_CC_1": "AM_CC_01", "AM_OFM_1": "AM_OFM_01"}.items():
            self.assertEqual(self.client.get("/steps/" + old).json()["code"], new)
        self.steps["AM_1"]["options"][0]["next step"] = "AM_CC_1"
        self.assertEqual(self.client.get("/steps/AM_1").json()["options"][0]["next step"], "AM_CC_01")

    def test_missing_step(self):
        self.assertEqual(self.client.get("/steps/unknown").status_code, 404)

    def test_feedback_and_retry_do_not_duplicate(self):
        for code, kind in [("FB_ES_01", "suggestion"), ("FB_FR_01", "complaint"), ("FB_EE_01", "compliment")]:
            payload = {"submission_id": str(uuid4()), "step_code": code, "comment": " Minha mensagem ", "chat_history": ["FB_01", code]}
            self.assertEqual(self.client.post("/chatbot/answers", json=payload).json(), {"saved": True})
            self.assertEqual(self.client.post("/chatbot/answers", json=payload).status_code, 200)
            self.assertEqual(self.answers[payload["submission_id"]]["type"], kind)
            self.assertEqual(self.answers[payload["submission_id"]]["comment"], "Minha mensagem")
        self.assertEqual(len(self.answers), 3)

    def test_ratings(self):
        for code in ["AM_CC_07", "AM_OFM_07", "MI_CC_16"]:
            for score in [1, 5]:
                payload = {"submission_id": str(uuid4()), "step_code": code, "score": score}
                self.assertEqual(self.client.post("/chatbot/answers", json=payload).status_code, 200)
                self.assertEqual(self.answers[payload["submission_id"]]["score"], score)

    def test_simple_submission_identifier(self):
        payload = {"submission_id": "envio-teste-1", "step_code": "FB_ES_01", "comment": "Minha mensagem"}
        self.assertEqual(self.client.post("/chatbot/answers", json=payload).status_code, 200)
        self.assertEqual(self.client.post("/chatbot/answers", json=payload).status_code, 200)
        self.assertEqual(len(self.answers), 1)
        payload["submission_id"] = ""
        self.assertEqual(self.client.post("/chatbot/answers", json=payload).status_code, 422)

    def test_invalid_answers_do_not_save(self):
        invalid = [
            {"step_code": "FB_FR_01", "comment": "   "},
            {"step_code": "FB_ES_01", "comment": "x" * 2001},
            {"step_code": "AM_CC_07"},
            {"step_code": "AM_CC_07", "score": 0},
            {"step_code": "AM_CC_07", "score": 6},
            {"step_code": "AM_CC_07", "score": 1.5},
            {"step_code": "AM_1", "comment": "Texto"},
            {"step_code": "unknown", "comment": "Texto"},
        ]
        for value in invalid:
            response = self.client.post("/chatbot/answers", json={"submission_id": str(uuid4()), **value})
            self.assertIn(response.status_code, [400, 404, 422])
        self.assertEqual(self.answers, {})

    def test_database_unavailable(self):
        self.database.db.step.find_one.side_effect = PyMongoError("offline")
        self.assertEqual(self.client.get("/steps/AM_1").status_code, 503)

    def test_failed_save_is_not_success(self):
        self.database.db.rating.update_one.side_effect = PyMongoError("offline")
        response = self.client.post("/chatbot/answers", json={"submission_id": str(uuid4()), "step_code": "FB_FR_01", "comment": "Texto"})
        self.assertEqual(response.status_code, 503)
        self.assertEqual(self.answers, {})

    def test_cors_allows_submission(self):
        response = self.client.options("/chatbot/answers", headers={"Origin": "http://localhost:5500", "Access-Control-Request-Method": "POST", "Access-Control-Request-Headers": "content-type"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["access-control-allow-origin"], "http://localhost:5500")


if __name__ == "__main__":
    unittest.main()
