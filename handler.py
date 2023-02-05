from random import randint
from create import dp
from aiogram import types
from keyboards import kb_main_menu
import spy


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    img = open('photo\\girl.jpeg', 'rb')
    await message.answer_photo(img)
    spy.spy(message)
    await message.answer(f'Привет, {message.from_user.first_name}, давай поиграем? ))')
    await message.answer('Пока у нас на выбор такие игры:', reply_markup=kb_main_menu)


@dp.message_handler(commands=['Правила'])
async def mes_sweets(message: types.Message):
    spy.spy(message)
    await message.answer('Сейчас расскажу правила:\n \n'
                         '🍬ИГРА КОНФЕТКИ!!!\n '
                         '🍬 На столе лежит определенное случайным образом количество конфет.\n'
                         '🍬 Играют два игрока - я и ты. Делаем ход по очереди.\n'
                         '🍬 Первый ход определяется жеребьёвкой.\n'
                         '🍬 За один ход можно взять не более чем 28 конфет.\n'
                         '🍬 Все конфеты оппонента достаются сделавшему последний ход.\n \n '
                         '🍬 Может, поддашься? Я известная сладкоежка ;)\n \n \n'
                         '❌⭕КРЕСТИКИ-НОЛИКИ!\n'
                         'Думаю, что правила ты знаешь.\n '
                         '❌⭕Первый ход определяется жеребьёвкой.\n \n')
    #await mes_start(message)



@dp.message_handler(commands=['Крестики-нолики'])
async def mes_idontknow(message: types.Message):
    spy.spy(message)
    await message.answer(f'Упс, это {message.text} я еще не умею обрабатывать. Начни сначала? /start')


@dp.message_handler(commands=['Конфетки'])
async def mes_sweets(message: types.Message):
    spy.spy(message)
    global number_of_candies
    number_of_candies = randint(50, 150)
    await message.answer(f"Количество конфет задано случайным образом и равно {number_of_candies}.")
    turn = randint(1, 2)
    if turn == 1:
        await message.answer(f"Первый ход определен жеребьевкой: ходит {message.from_user.first_name}!\n"
                             f"Введи количество конфет от 1 до 28, которое ты хочешь взять")

    else:
        await message.answer(f"Первый ход определен жеребьевкой: ходит Бот!")
        await message.answer(f'Мы с ботом берем {bot_turn()} 🍬\n'
                             f'На столе осталось {number_of_candies}.'
                             f'Теперь твой ход, {message.from_user.first_name}!')
    await sweets_game(message)


@dp.message_handler()
async def sweets_game(message: types.Message):
    global number_of_candies
    if message.text.isdigit():
        if int(message.text) in range(1, 29) and number_of_candies - int(message.text) > -1:
            number_of_candies -= int(message.text)
            await message.answer(f'Ты взял {message.text} 🍬. На столе осталось {number_of_candies} 🍬.\n ')
            if number_of_candies == 0:
                await message.answer(
                    f'Поздравляю, {message.from_user.first_name}, победа за тобой! Смотри, теперь не лопни 😉')

                return
            await message.answer(f'Теперь очередь Бота!')
            await message.answer(f'Мы с ботом берем {bot_turn()} 🍬! На столе осталось {number_of_candies} ')
            if number_of_candies == 0:
                await message.answer(f'{message.from_user.first_name}, Бот выиграл! Все конфетки мои! Приходи на чай 😉')

                return
            await message.answer(f'Теперь твой ход, {message.from_user.first_name}!')
        else:
            await message.answer(f'Играй по правилам ) Введи количество конфет, от 1 до 28 штук! \n'
                                 f'А еще - на столе не может остаться отрицательное количество конфет!')



def bot_turn():
     global number_of_candies
     if number_of_candies < 28:
         bot_took = number_of_candies
     else:
         bot_took = number_of_candies % 29
         if bot_took == 0:
             bot_took = 1
     number_of_candies -= bot_took
     return bot_took

number_of_candies = 0


