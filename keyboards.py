from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_sweets = KeyboardButton('/Конфетки')
btn_ttt = KeyboardButton('/Крестики-нолики')
btn_rules = KeyboardButton('/Правила')

kb_main_menu.add(btn_sweets, btn_ttt)
kb_main_menu.add(btn_rules)
