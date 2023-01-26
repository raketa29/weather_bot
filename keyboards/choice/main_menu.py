from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_help = KeyboardButton("/help")
btn_back = KeyboardButton("/back")
btn_menu = KeyboardButton("/menu")

main_menu.add(btn_help, btn_menu, btn_back)
