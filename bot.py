import emoji
from aiogram import Bot, Dispatcher, types, executor
from auth.config import API_TOKEN
import logging
from aiogram.types import Message
from keyboards.choice.main_menu import main_menu as nav
from keyboards.choice.weather_menu import weather_menu as weather_nav
from app.get_weather import RusWeather

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

HELP_TEXT = """
            <b> /start</b> - <em> старт бота </em>
            <b> /back </b> - <em>возврат к выбору функций</em>
            <b> /menu </b> - <em> основное меню(основные функции)</em>
            """


@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await bot.send_message(message.from_id,
                           text=f"Привет {message.from_user.first_name}!\nВыбери одну из функций из меню:",
                           reply_markup=nav)
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: Message):
    await bot.send_message(message.from_user.id, text=HELP_TEXT, reply_markup=nav)
    await message.delete()


@dp.message_handler(commands=["menu"])
async def menu_command(message: Message):
    await bot.send_message(message.from_user.id, text=f"{emoji.emojize(':toolbox:')} Меню {emoji.emojize(':toolbox:')}",
                           reply_markup=weather_nav)
    await message.delete()


@dp.message_handler()
async def answer_city(message: Message):
    city = message.text.strip().title()
    rw = RusWeather(city)
    await message.answer(rw.weather_info_str)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
