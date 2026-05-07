import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ВСТАВ СВІЙ ТОКЕН НИЖЧЕ (між лапками)
API_TOKEN = 'ТУТ_ТВІЙ_ТОКЕН_ВІД_BOTFATHER'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def get_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Камінь 🪨")
    builder.button(text="Ножиці ✂️")
    builder.button(text="Папір 📄")
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Обирай свій хід:", reply_markup=get_keyboard())

@dp.message(F.text.in_({"Камінь 🪨", "Ножиці ✂️", "Папір 📄"}))
async def play_game(message: types.Message):
    choices = ["Камінь 🪨", "Ножиці ✂️", "Папір 📄"]
    bot_choice = random.choice(choices)
    user_choice = message.text

    if user_choice == bot_choice:
        res = "Нічия! 🤝"
    elif (user_choice == "Камінь 🪨" and bot_choice == "Ножиці ✂️") or \
         (user_choice == "Ножиці ✂️" and bot_choice == "Папір 📄") or \
         (user_choice == "Папір 📄" and bot_choice == "Камінь 🪨"):
        res = "Ти виграв! 🎉"
    else:
        res = "Я виграв! 🤖"

    await message.answer(f"Мій хід: {bot_choice}\n{res}", reply_markup=get_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
