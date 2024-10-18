from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import keyboards.keyboards as keyboard
from handlers.states import Register

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=keyboard.main)
    await message.reply('How do you do?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('You tap by "help" button.')


@router.message(F.text == 'Catalog')
async def cmd_catalog(message: Message):
    await message.answer(text='Select product: ', reply_markup=keyboard.catalog)


# keyboard handler
@router.callback_query(F.data == 'product1_id1')
async def product(callback: CallbackQuery):
    await callback.answer('This product was been add to basket', show_alert=True)
    await callback.message.answer('This product was been add to basket')


# register helper
@router.message(Command('register'))
async def cmd_register(message: Message, state: FSMContext):
    await state.set_state(Register.first_name)
    await message.answer('Input your first name')


@router.message(Register.first_name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Register.age)
    await message.answer('Input your age')


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Input your number', reply_markup=keyboard.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    # get user info
    data = await state.get_data()
    await message.answer(f'First name: {data["first_name"]}, Age: {data["age"]}, Number: {data["number"]}')
    await state.clear()


