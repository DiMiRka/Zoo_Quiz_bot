from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from text import share_message
from text import animals_text
from aiogram.fsm.state import State, StatesGroup

from utils import result_animal

kb_1 = [
    [types.KeyboardButton(text='Индия'),
     types.KeyboardButton(text='Вьетнам'),
     types.KeyboardButton(text='Испания'),
     types.KeyboardButton(text='Китай'),
     types.KeyboardButton(text='Канада')]
]
question_kb_1 = ReplyKeyboardBuilder(kb_1)
question_kb_1.adjust(1)

kb_2 = [
    [types.KeyboardButton(text='Светлый лес'),
     types.KeyboardButton(text='Горы в гималаях'),
     types.KeyboardButton(text='У водоёма'),
     types.KeyboardButton(text='Широкое поле')]
]
question_kb_2 = ReplyKeyboardBuilder(kb_2)
question_kb_2.adjust(1)

kb_3 = [
    [types.KeyboardButton(text='Мощь и сила'),
     types.KeyboardButton(text='Миролюбивость'),
     types.KeyboardButton(text='Осторожность и любознательность'),
     types.KeyboardButton(text='Застенчивость'),
     types.KeyboardButton(text='Грациозность')]
]
question_kb_3 = ReplyKeyboardBuilder(kb_3)
question_kb_3.adjust(1)

kb_4 = [
    [types.KeyboardButton(text='Фрукты'),
     types.KeyboardButton(text='Орехи'),
     types.KeyboardButton(text='Винегрет'),
     types.KeyboardButton(text='Мясо')]
]
question_kb_4 = ReplyKeyboardBuilder(kb_4)
question_kb_4.adjust(1)

kb_5 = [
    [types.KeyboardButton(text='В коллективе, люблю общение'),
     types.KeyboardButton(text='В одиночестве, предпочитаю оставаться наедине со своими мыслями')]
]
question_kb_5 = ReplyKeyboardBuilder(kb_5)
question_kb_5.adjust(1)

kb_6 = [
    [types.KeyboardButton(text='В холоде со снежком'),
     types.KeyboardButton(text='В тепле мне куда лучше'),
     types.KeyboardButton(text='Не имеет значения, везде хорошо')]
]
question_kb_6 = ReplyKeyboardBuilder(kb_6)
question_kb_6.adjust(1)

kb_7 = [
    [types.KeyboardButton(text='Белый'),
     types.KeyboardButton(text='Серый'),
     types.KeyboardButton(text='Зеленый'),
     types.KeyboardButton(text='Оранжевый')]
]
question_kb_7 = ReplyKeyboardBuilder(kb_7)
question_kb_7.adjust(1)

kb_8 = [
    [types.KeyboardButton(text='Искусный рыболов это про меня'),
     types.KeyboardButton(text='Рыбалка не моё')]
]
question_kb_8 = ReplyKeyboardBuilder(kb_8)
question_kb_8.adjust(1)

kb_9 = [
    [types.KeyboardButton(text='Люблю вставать пораньше, чтобы побольше успеть'),
     types.KeyboardButton(text='По душе поспать, а потом всю ночь бодрствовать'),
     types.KeyboardButton(text='Живу в обычном ритме, не отдавая предпочтений')]
]
question_kb_9 = ReplyKeyboardBuilder(kb_9)
question_kb_9.adjust(1)

kb_10 = [
    [types.KeyboardButton(text='Люблю поваляться, чем меньше дел тем лучше'),
     types.KeyboardButton(text='Стараюсь не сидеть на месте, хочу везде и сразу')]
]
question_kb_10 = ReplyKeyboardBuilder(kb_10)
question_kb_10.adjust(1)


async def make_menu(share_text):
    kb_menu = [
        [types.InlineKeyboardButton(text='Попробовать еще раз?', callback_data='начать викторину заново')],
        [types.InlineKeyboardButton(text='Поделиться результатом в VK', url=f'{share_message}{share_text}')],
        [types.InlineKeyboardButton(text='Связаться зоопарком', callback_data='связь')],
        [types.InlineKeyboardButton(text='Оставить отзыв о боте', callback_data='отзыв')]
    ]
    menu = InlineKeyboardMarkup(inline_keyboard=kb_menu, resize_keyboard=True)
    return menu


async def make_call(text_share):
    kb_call = [[types.KeyboardButton(text=f'Чат с сотрудником \n Результат викторины:\n {text_share}')]]
    call_kb = ReplyKeyboardMarkup(keyboard=kb_call, resize_keyboard=True)
    return call_kb
