from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Buy')],
                                     [KeyboardButton(text='Contacts'), KeyboardButton(text="About us")]],
                           resize_keyboard=True, input_field_placeholder='PLease select option...')

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='product1', callback_data='product1_id1')],
                                                [InlineKeyboardButton(text='product2', callback_data='product2_id2')],
                                                [InlineKeyboardButton(text='product3', callback_data='product3_id3')],
                                                [InlineKeyboardButton(text='product4', callback_data='product4_id4')],
                                                [InlineKeyboardButton(text='product5', callback_data='product5_id5')],
                                                [InlineKeyboardButton(text='product6', callback_data='product6_id6')],
                                                [InlineKeyboardButton(text='product7', callback_data='product7_id7')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send number', request_contact=True)]], resize_keyboard=True)
