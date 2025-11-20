from telegram.ext import ApplicationBuilder
from app.config import Config
from app.handlers.start import start_handler
from app.handlers.menu import menu_handler
from app.handlers.consultas import consulta_message_handler

def create_bot():
    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Handlers centrais
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(consulta_message_handler)

    return app