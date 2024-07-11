from aiogram import F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup

from utils import *
from text import *
from kb import *

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
    await message.answer('В какой стране ты хотел(а) бы побывать?', reply_markup=question_kb_1.as_markup())
    await state.set_state(Quiz.waiting_question_1.state)


@router_1.message(Quiz.waiting_question_1)
async def question_2(message: types.Message, state: FSMContext):
    await question_answer_1(message.text)
    await message.answer('Побывав в каком месте, ты чувствуешь новый приток сил?',
                         reply_markup=question_kb_2.as_markup())
    await state.set_state(Quiz.waiting_question_2.state)


@router_1.message(Quiz.waiting_question_2)
async def question_3(message: types.Message, state: FSMContext):
    await question_answer_2(message.text)
    await message.answer('Что тебе ближе?', reply_markup=question_kb_3.as_markup())
    await state.set_state(Quiz.waiting_question_3.state)


@router_1.message(Quiz.waiting_question_3)
async def question_4(message: types.Message, state: FSMContext):
    await question_answer_3(message.text)
    await message.answer('Что бы ты съел(а)?', reply_markup=question_kb_4.as_markup())
    await state.set_state(Quiz.waiting_question_4.state)


@router_1.message(Quiz.waiting_question_4)
async def question_5(message: types.Message, state: FSMContext):
    await question_answer_4(message.text)
    await message.answer('Какое времяпровождение тебе по душе?', reply_markup=question_kb_5.as_markup())
    await state.set_state(Quiz.waiting_question_5.state)


@router_1.message(Quiz.waiting_question_5)
async def question_6(message: types.Message, state: FSMContext):
    await question_answer_5(message.text)
    await message.answer('В каком климате тебе комфортнее?', reply_markup=question_kb_6.as_markup())
    await state.set_state(Quiz.waiting_question_6.state)


@router_1.message(Quiz.waiting_question_6)
async def question_7(message: types.Message, state: FSMContext):
    await question_answer_6(message.text)
    await message.answer('Какой цвет тебе нравится больше?', reply_markup=question_kb_7.as_markup())
    await state.set_state(Quiz.waiting_question_7.state)


@router_1.message(Quiz.waiting_question_7)
async def question_8(message: types.Message, state: FSMContext):
    await question_answer_7(message.text)
    await message.answer('Как ты относишься к рыбалке?', reply_markup=question_kb_8.as_markup())
    await state.set_state(Quiz.waiting_question_8.state)


@router_1.message(Quiz.waiting_question_8)
async def question_9(message: types.Message, state: FSMContext):
    await question_answer_8(message.text)
    await message.answer('На какой период дня приходится твоя активность?', reply_markup=question_kb_9.as_markup())
    await state.set_state(Quiz.waiting_question_9.state)


@router_1.message(Quiz.waiting_question_9)
async def question_10(message: types.Message, state: FSMContext):
    await question_answer_9(message.text)
    await message.answer('Как ты проводишь свободное время?', reply_markup=question_kb_10.as_markup())
    await state.set_state(Quiz.waiting_question_10.state)


@router_1.message(Quiz.waiting_question_10)
async def result(message: types.Message, state: FSMContext):
    await question_answer_10(message.text)
    animal, animal_id = result_animal()
    text_share = animals_text[animal]
    await message.answer_animation(animation=animal_id, reply_markup=ReplyKeyboardRemove(),
                                   caption=text_share, show_caption_above_media=True)
    await message.answer(
        f'Вы можете взять под опеку своё животное, для получения подробной информации перейдите по ссылке'
        f'\n {link_text}', reply_markup=await make_menu(share_text=text_share))
    await state.set_data({'share': text_share})


@router_1.callback_query(F.data == 'начать викторину заново')
async def new_quiz(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('В какой стране ты хотел(а) бы побывать?', reply_markup=question_kb_1.as_markup())
    await state.set_state(Quiz.waiting_question_1.state)
