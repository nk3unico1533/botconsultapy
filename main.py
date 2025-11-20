from app.bot import create_bot
import asyncio

if __name__ == "__main__":
    app = create_bot()
    asyncio.run(app.run_polling())
