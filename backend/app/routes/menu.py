from fastapi import APIRouter, HTTPException

from pymongo.errors import PyMongoError
from app.repositories.chatbot import find_step, save_answer
from app.schemas.chatbot import ChatbotAnswer
from app.repositories.service import find_available_services, find_support_title, find_services_descriptions

router = APIRouter()


# rota para retornar o nome dos serviços encontrados no site: Atende+ e meu INSS
@router.get("/services")
def services():
    result = find_available_services()
    return [service["name"] for service in result]

# rota para retornar o nome usado no botão de suporte
@router.get("/support")
def support():
    result = find_support_title()
    return [service["name"] for service in result]


@router.get("/services/descriptions")
def services_descriptions():
    result = find_services_descriptions()
    return [service["description"] for service in result]


def get_step(code):
    try:
        result = find_step(code)
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Não foi possível consultar o chatbot.")
    if result is None:
        raise HTTPException(status_code=404, detail="Etapa não encontrada.")
    return result


def check_answer(answer, step):
    if not step.get("input_type"):
        raise HTTPException(status_code=400, detail="Esta etapa não recebe respostas escritas ou notas.")

    if step["input_type"] == "comment" and answer.comment.strip() == "":
        raise HTTPException(status_code=422, detail="Escreva sua mensagem antes de enviar.")

    if step["input_type"] == "score" and answer.score is None:
        raise HTTPException(status_code=422, detail="Escolha uma nota de 1 a 5.")


@router.get("/steps/{code}")
def chatbot_step(code: str):
    return get_step(code)


@router.post("/chatbot/answers")
def chatbot_answer(answer: ChatbotAnswer):
    step = get_step(answer.step_code)
    check_answer(answer, step)

    data = {
        "type": step["feedback_type"],
        "step_code": step["code"],
        "comment": answer.comment.strip(),
        "score": None,
        "chat_history": answer.chat_history,
    }

    if step["input_type"] == "score":
        data["score"] = answer.score

    try:
        save_answer(answer.submission_id, data)
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Não foi possível salvar. Sua resposta não foi confirmada; tente novamente.")
    return {"saved": True}


