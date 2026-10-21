from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo.errors import PyMongoError
from app.repositories.chatbot import find_step, save_answer
from app.schemas.chatbot import ChatbotAnswer
from app.repositories.service import find_available_services, find_support_title, find_services_descriptions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# rota para retornar o nome dos serviços encontrados no site: Atende+ e meu INSS
@app.get("/services")
def services():
    result = find_available_services()
    return [service["name"] for service in result]

# rota para retornar o nome usado no botão de suporte
@app.get("/support")
def support():
    result = find_support_title()
    return [service["name"] for service in result]


@app.get("/services/descriptions")
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


@app.get("/steps/{code}")
def chatbot_step(code: str):
    return get_step(code)


@app.post("/chatbot/answers")
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


