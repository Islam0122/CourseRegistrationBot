from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.text import questions

router_direction = Router()

class CommandDirections(StatesGroup):
    quiz = State()
    correct_answers = State()
    wrong_answers = State()

def make_question_keyboard(question):
    builder = InlineKeyboardBuilder()
    for text, correct in question["options"]:
        builder.add(InlineKeyboardButton(text=text, callback_data=str(correct)))
    return builder.as_markup()

@router_direction.callback_query(F.data == "backend")
async def back_direction(query: CallbackQuery, state: FSMContext):
    await state.update_data(question_index=0, correct_answers=0, wrong_answers=0)
    await state.set_state(CommandDirections.quiz)

    question = questions[0]
    keyboard = make_question_keyboard(question)
    await query.message.answer(
        text=question["text"],
        reply_markup=keyboard
    )
    await query.answer()

@router_direction.callback_query(F.data.in_({"True","False"}))
async def answer_question(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data.get("question_index", 0)
    correct_count = data.get("correct_answers", 0)
    wrong_count = data.get("wrong_answers", 0)

    if query.data == "True":
        correct_count += 1
        await query.answer("✅ Правильно!")
    else:
        wrong_count += 1
        await query.answer("❌ Неправильно!")

    await state.update_data(correct_answers=correct_count, wrong_answers=wrong_count)

    index += 1
    if index >= len(questions):
        await query.message.answer(
            text=f"Викторина завершена!\n✅ Правильных: {correct_count}\n❌ Неправильных: {wrong_count}"
        )
        await state.clear()
    else:
        await state.update_data(question_index=index)
        question = questions[index]
        keyboard = make_question_keyboard(question)
        await query.message.answer(
            text=question["text"],
            reply_markup=keyboard
        )