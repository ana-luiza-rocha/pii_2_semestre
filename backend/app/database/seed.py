"""Carrega os dados iniciais. Cada execucao pode adicionar documentos repetidos."""

from app.database.database import client, close_connection


if __name__ == "__main__":
    try:
        client.admin.command("ping")

        # Cada modulo executa a insercao que ja existe no seu arquivo.
        import app.repositories.service

        import app.repositories.atende_mais.options
        import app.repositories.atende_mais.create_account
        import app.repositories.atende_mais.get_medical_forms

        import app.repositories.meu_inss.options
        import app.repositories.meu_inss.account_creation

        import app.repositories.feedback.options
        import app.repositories.feedback.complaint
        import app.repositories.feedback.compliment
        import app.repositories.feedback.suggestion

        print("Todos os dados foram inseridos!", flush=True)
    finally:
        close_connection()
