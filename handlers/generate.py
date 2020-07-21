from aiogram import types
from setup import dp, bot
from keyboards.generate_kb import (
    generate_action_kb,
    generate_choice_kb
)
from services import mrbeamapi
import random


@dp.message_handler(commands=["generate"])
async def cmd_new(message: types.Message):
    await message.reply("Select complexity for random beam", reply_markup=generate_choice_kb)


@dp.callback_query_handler(text_contains="generate")
async def process_beam_generation(callback_query: types.CallbackQuery):
    complexity = callback_query.data.split(":")[-1]
    beam_list = mrbeamapi.random_beam(complexity)

    beam = "Your <b>" + complexity + "</b> beam is ready!\nLook what we've got here 👇:\n\n"
    for element in beam_list:
        beam = beam + "'" + str(element["type"]) + "'" + " at x=" + str(element["x"])
        if element["type"] == "force" or element["type"] == "distload":
            beam = beam + " with value " + str(element["value"]) + "\n\n"
        else:
            beam = beam + "\n\n"

    beam += "\nWhat to do next?"
    # await callback_query.message.answer(beam)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=beam,
        reply_markup=generate_action_kb)

# TODO: add states
@dp.callback_query_handler(text_contains="action")
async def process_beam_action(callback_query: types.CallbackQuery):
    action = callback_query.data.split(":")[-1]
    if action == "calculate":
        if random.random() < 0.3:
            answer = "Starting to calculate ⛏. \nOh, hard beam. Pridetsya poebat'sya!"
            keyboard = types.ReplyKeyboardRemove()
        else:
            answer = "Starting to calculate ⛏. Wait a minute.."
            keyboard = types.ReplyKeyboardRemove()
    elif action == "edit":
        answer = "Sorry, this function is not implemented yet 😞"
        keyboard = types.ReplyKeyboardRemove()
    else:
        answer = "Ok, let's try with another beam!\nSelect complexity:"
        keyboard = generate_choice_kb

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=answer,
        reply_markup=keyboard)

