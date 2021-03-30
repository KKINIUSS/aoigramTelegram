from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, cancel
from aiogram.dispatcher.filters import Command

from loader import dp
@dp.message_handler(CommandStart())
async def show_menu(message: Message):
    await message.answer(f"Вас приветствует бот-помощник ЖК!")
    await message.answer("Пожалуйста, выберите пункт из меню", reply_markup=menu)


@dp.message_handler(text="отмена", state="*")
async def back_from_reg(message: Message, state=FSMContext):
    await state.finish()
    await message.answer("Вы вернулись в главное меню", reply_markup=menu)


