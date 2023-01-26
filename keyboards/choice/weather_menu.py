from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

weather_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

btn_Krakow = KeyboardButton("Krakow")
btn_Wielizhka = KeyboardButton("Wielizhka")
btn_Dnipro = KeyboardButton("Dnipro")
btn_Rivne = KeyboardButton("Rivne")

weather_menu.add(btn_Krakow, btn_Wielizhka, btn_Dnipro, btn_Rivne)