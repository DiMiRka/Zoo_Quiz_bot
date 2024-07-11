from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.fsm.state import State, StatesGroup

from kb import make_call
from utils import result_animal
from text import animals_text

router_2 = Router()


class Zoo(StatesGroup):
    text_to_stuff = State()
    text_to_review = State()


@router_2.callback_query(F.data == 'связь')
async def call(callback: types.CallbackQuery, state: FSMContext):
    animal, animal_id = result_animal()
    text_share = animals_text[animal]
    user_name = callback.from_user.username
    await callback.message.answer(f'Связаться с нашим сотрудником, Дмитрием: \n\n'
                                  f'telegram: https://t.me/dimirka_94\n'
                                  f'E-mail: fallen_94@bk.ru\n'
                                  f'Phone: 8-914-541-23-19', reply_markup=await make_call(text_share, user_name))
    await state.set_state(Zoo.text_to_stuff)
    await callback.answer()


@router_2.message(Zoo.text_to_stuff)
async def text_to_stuff(message: types.Message, state: FSMContext):
    await message.copy_to(chat_id=415148449, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router_2.callback_query(F.data == 'отзыв')
async def review(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(f'Пожалуйста напишите Ваше мнение о нашем боте: ')
    await state.set_state(Zoo.text_to_review)
    await callback.answer()


@router_2.message(Zoo.text_to_review)
async def text_to_review(message: types.Message, state: FSMContext):
    with open('review.txt', 'a') as f:
        f.write(f'{message.from_user.username}: {message.text}\n\n')
    await state.clear()
