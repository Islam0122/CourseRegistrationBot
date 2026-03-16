from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.question_for_command import questions_for_frontend
from keyboards.command_inline import keyboard_back

router_frontend = Router()

class FrontendState(StatesGroup):
    question = State()

@router_frontend.callback_query(F.data == "frontend")
async def frontend(query: CallbackQuery, state: FSMContext):
    await state.update_data(q_index=0, score=0)
    data = await state.get_data()
    q = questions_for_frontend[data["q_index"]]
    kb = InlineKeyboardBuilder()
    for i in q["options"]:
        kb.add(InlineKeyboardButton(text=i, callback_data=i[0]))
    kb.adjust(1)
    await query.message.answer(text=q["text"], reply_markup=kb.as_markup())
    await state.set_state(FrontendState.question)

@router_frontend.callback_query(FrontendState.question, F.data.in_(["A", "B", "C"]))
async def question(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    q_index = int(data["q_index"])
    score = int(data["score"])
    q = questions_for_frontend[data["q_index"]]
    if query.data[0] == q["correct_answer"]:
        score += 1
    q_index += 1
    if q_index >= len(questions_for_frontend):
        await query.message.answer(text=f"Правильных ответов: {str(score)}", reply_markup=keyboard_back)
        await state.clear()
        return
    await state.update_data(q_index=q_index, score=score)
    q1 = questions_for_frontend[q_index]
    kb = InlineKeyboardBuilder()
    for i in q1["options"]:
        kb.add(InlineKeyboardButton(text=i, callback_data=i[0]))
    kb.adjust(1)
    await query.message.answer(text=q1["text"], reply_markup=kb.as_markup())