from aiogram import executor
from handler import dp

async def on_start(_):
    print('Бот запущен')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)