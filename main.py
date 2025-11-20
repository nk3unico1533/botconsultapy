import os
import asyncio
from aiohttp import web
from app.bot import create_bot

async def start_bot():
    app = create_bot()
    await app.run_polling()

async def webserver():
    async def handle(request):
        return web.Response(text="Bot está rodando 🚀")

    app = web.Application()
    app.router.add_get("/", handle)

    port = int(os.environ.get("PORT", 8000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    await asyncio.gather(
        start_bot(),
        webserver()
    )

if __name__ == "__main__":
    asyncio.run(main())