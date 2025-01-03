from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.logger import log
from bot.states.user_states import USER_STATE


async def recipe(update: Update, context: CallbackContext) -> None:
    log(update)
    chat_id = update.effective_chat.id
    USER_STATE[chat_id] = 'recipe'
    await update.message.reply_text("Вы выбрали: Составить рецепт. Опишите, что хотите приготовить или введите список продуктов.")
