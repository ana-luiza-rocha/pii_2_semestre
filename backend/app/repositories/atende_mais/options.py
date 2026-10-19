from database import db
from collections import step

atende_mais_options = {

    "code": "AM_1",
    "service_name": "Atende+",
    "message": "O que você deseja fazer no Atende+ hoje?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "AM_CC_1"
        }, 

        {
            "text": "Obter ficha médica",
            "next step": "AM_OFM_1"
        }, 

        {
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}