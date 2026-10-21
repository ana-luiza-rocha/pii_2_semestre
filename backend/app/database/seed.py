"""Carrega ou atualiza os dados iniciais usando o campo code."""

from app.database.database import client, close_connection


if __name__ == "__main__":
    try:
        client.admin.command("ping")

        # Cada modulo insere ou atualiza os documentos pelo campo code.
        print("00/10")
        import app.repositories.service

        print("01/10")
        import app.repositories.atende_mais.options

        print("02/10")
        import app.repositories.atende_mais.create_account

        print("03/10")
        import app.repositories.atende_mais.get_medical_forms

        print("04/10")
        import app.repositories.meu_inss.options

        print("05/10")
        import app.repositories.meu_inss.account_creation

        print("06/10")
        import app.repositories.feedback.options

        print("07/10")
        import app.repositories.feedback.complaint

        print("08/10")
        import app.repositories.feedback.compliment

        print("09/10")
        import app.repositories.feedback.suggestion

        print("10/10")

        print("Todos os dados foram inseridos ou atualizados!", flush=True)
    finally:
        close_connection()
