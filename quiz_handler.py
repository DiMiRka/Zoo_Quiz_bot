import aiohttp

from datetime import datetime

from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types

from utils import *

router_1 = Router()


class Quiz(StatesGroup):
    waiting_question_1 = State()
    waiting_question_2 = State()
    waiting_question_3 = State()
    waiting_question_4 = State()
    waiting_question_5 = State()
    waiting_question_6 = State()
    waiting_question_7 = State()
    waiting_question_8 = State()
    waiting_question_9 = State()
    waiting_question_10 = State()


@router_1.message(F.text.lower() == 'начать викторину!')
async def quiz_start(message: types.Message, state: FSMContext):
    kb = [
        [types.KeyboardButton(text='Индия'),
         types.KeyboardButton(text='Вьетнам'),
         types.KeyboardButton(text='Испания'),
         types.KeyboardButton(text='Китай'),
         types.KeyboardButton(text='Канада')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('В какой стране ты хотел(а) бы побывать?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_1.state)


@router_1.message(Quiz.waiting_question_1)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_1(message.text)})
    kb = [
        [types.KeyboardButton(text='Светлый лес'),
         types.KeyboardButton(text='Горы в гималаях'),
         types.KeyboardButton(text='У водоёма'),
         types.KeyboardButton(text='Широкое поле')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Побывав в каком месте, ты чувствуешь новый приток сил?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_2.state)


@router_1.message(Quiz.waiting_question_2)
async def question_3(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_2(message.text)})
    kb = [
        [types.KeyboardButton(text='Мощь и сила'),
         types.KeyboardButton(text='Миролюбивость'),
         types.KeyboardButton(text='Осторожность и любознательность'),
         types.KeyboardButton(text='Застенчивость'),
         types.KeyboardButton(text='Грациозность')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Что тебе ближе?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_3.state)


@router_1.message(Quiz.waiting_question_3)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_3(message.text)})
    kb = [
        [types.KeyboardButton(text='Фрукты'),
         types.KeyboardButton(text='Орехи'),
         types.KeyboardButton(text='Винегрет'),
         types.KeyboardButton(text='Мясо')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Что бы ты съел(а)?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_4.state)


@router_1.message(Quiz.waiting_question_4)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_4(message.text)})
    kb = [
        [types.KeyboardButton(text='В коллективе, люблю общение'),
         types.KeyboardButton(text='В одиночестве, предпочитаю оставаться наедине со своими мыслями')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Какое времяпровождение тебе по душе?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_5.state)


@router_1.message(Quiz.waiting_question_5)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_5(message.text)})
    kb = [
        [types.KeyboardButton(text='В холоде со снежком'),
         types.KeyboardButton(text='В тепле мне куда лучше'),
         types.KeyboardButton(text='Не имеет значения, везде хорошо')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('В каком климате тебе комфортнее?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_6.state)


@router_1.message(Quiz.waiting_question_6)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_6(message.text)})
    kb = [
        [types.KeyboardButton(text='Белый'),
         types.KeyboardButton(text='Серый'),
         types.KeyboardButton(text='Зеленый'),
         types.KeyboardButton(text='Оранжевый')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Какой цвет тебе нравится больше?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_7.state)


@router_1.message(Quiz.waiting_question_7)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_7(message.text)})
    kb = [
        [types.KeyboardButton(text='Искусный рыболов это про меня'),
         types.KeyboardButton(text='Рыбалка не моё')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Как ты относишься к рыбалке?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_8.state)


@router_1.message(Quiz.waiting_question_8)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_8(message.text)})
    kb = [
        [types.KeyboardButton(text='Люблю вставать пораньше, чтобы побольше успеть'),
         types.KeyboardButton(text='По душе поспать, а потом всю ночь бодрствовать'),
         types.KeyboardButton(text='Живу в обычном ритме, не отдавая предпочтений')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('На какой период дня приходится твоя активность?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_9.state)


@router_1.message(Quiz.waiting_question_9)
async def question_2(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_8(message.text)})
    kb = [
        [types.KeyboardButton(text='Люблю поваляться, чем меньше дел тем лучше'),
         types.KeyboardButton(text='Стараюсь не сидеть на месте, хочу везде и сразу')]
    ]
    builder = ReplyKeyboardBuilder()
    for i in kb[0]:
        builder.add(i)
    builder.adjust(1)
    await message.answer('Как ты проводишь свободное время?', reply_markup=builder.as_markup())
    await state.set_state(Quiz.waiting_question_10.state)


@router_1.message(Quiz.waiting_question_10)
async def question_3(message: types.Message, state: FSMContext):
    await state.set_data({'Animals': question_answer_8(message.text)})
    animal, animal_id = result_animal()
    print(animal)
    await message.answer_animation(animation=animal_id,
                                   caption=f'Вы {animal}', show_caption_above_media=True)
    await message.answer(
        f'Вы можете взять под опеку своё животное, для получения подробной информации перейдите по ссылке'
        f'\n {link_text}')
