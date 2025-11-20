from telegram.ext import MessageHandler, filters
from app.services.consulta_cpf import consulta_cpf_api
from app.services.consulta_cnpj import consulta_cnpj_api
from app.utils.logging import log

user_state = {}

async def consulta_message_handler(update, context):
    user_id = update.message.from_user.id
    texto = update.message.text

    estado = user_state.get(user_id)

    # CPF
    if estado == "cpf":
        log(f"Consulta CPF — {user_id}")
        resposta = consulta_cpf_api(texto)
        await update.message.reply_text(resposta)
        user_state[user_id] = None
        return

    # CNPJ
    if estado == "cnpj":
        log(f"Consulta CNPJ — {user_id}")
        resposta = consulta_cnpj_api(texto)
        await update.message.reply_text(resposta)
        user_state[user_id] = None
        return

consulta_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, consulta_message_handler)
