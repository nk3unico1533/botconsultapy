from telegram.ext import CallbackQueryHandler
from app.utils.logging import log
from app.handlers.consultas import user_state

async def menu_handler(update, context):
    query = update.callback_query
    await query.answer()

    mod = query.data
    uid = query.from_user.id
    
    log(f"{uid} escolheu módulo: {mod}")

    if mod == "mod_cpf":
        user_state[uid] = "cpf"
        await query.edit_message_text("Digite o CPF:")

    elif mod == "mod_cnpj":
        user_state[uid] = "cnpj"
        await query.edit_message_text("Digite o CNPJ:")

    elif mod == "credits":
        await query.edit_message_text("💳 Você tem 10 créditos disponíveis.")

    elif mod == "support":
        await query.edit_message_text("📞 Suporte: @seuuser")

menu_handler = CallbackQueryHandler(menu_handler)
