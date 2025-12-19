from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
load_dotenv()
token = os.getenv('prueba_token')

async def decir_ip(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("svopmc.com")
async def comenzar(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenid@ al mejor servidor de Minecraft que podras encontrar, usa /ip (para poder ver la IP del servidor), tambien puedes usar /discord para ir a nuestro Discord oficial")
async def link_de_discord(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Unete a nuestro Discord: https://discord.gg/WSd9WT7fme")
aplicacion = ApplicationBuilder().token("8285635468:AAExfzIHqLDy-YiS-fDmjstX_guPQvkZ-cU").build()
aplicacion.add_handler(CommandHandler("start", comenzar))
aplicacion.add_handler(CommandHandler("ip", decir_ip))
aplicacion.add_handler(CommandHandler("discord", link_de_discord))
aplicacion.run_polling(allowed_updates=Update.ALL_TYPES)

