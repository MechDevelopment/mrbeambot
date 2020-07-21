from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


generate_choice_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Elementary", callback_data="generate:elementary"),
        InlineKeyboardButton(text="Intermediate", callback_data="generate:intermediate"),
        InlineKeyboardButton(text="Advanced", callback_data="generate:advanced"),
    ]
])

generate_action_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Calculate!", callback_data="action:calculate"),
        InlineKeyboardButton(text="Edit Beam", callback_data="action:edit"),
        InlineKeyboardButton(text="Generate again", callback_data="action:again")
    ]
])
