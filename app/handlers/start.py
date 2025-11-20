from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Consulta CPF", callback_data="mod_cpf")],
        [InlineKeyboardButton("Consulta CNPJ", callback_data="mod_cnpj")],
        [InlineKeyboardButton("Meus Créditos", callback_data="credits")],
        [InlineKeyboardButton("Suporte", callback_data="support")],
    ]
    
    await update.message.reply_text(
        "🚀 Bem-vindo ao Bot Premium!\nEscolha uma opção:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

start_handler = CommandHandler("start", start)
