from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сделать запрос"),
        ],
        [
            KeyboardButton(text="Регистрация"), KeyboardButton(text="Для сотрудников ЖК"),
        ],
    ],
    resize_keyboard=True
)

