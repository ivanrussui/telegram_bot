from aiogram import Bot, Dispatcher, executor, types

import python_weather

# bot init
bot = Bot(token='5295298689:AAFqeXLg7IWydspmPpg7CFRiWqErq3Z5v84')
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

# echo бот - погода
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = (weather.current.temperature - 32) * 5 / 9

    resp_msg = weather.location_name + '\n'
    resp_msg += f'Текущая температура: {round(celsius)}°\n'
    resp_msg += f'Состояние погоды: {weather.current.sky_text}'

    if celsius <= 10:
        resp_msg += '\n\nНа улице прохладно'
    else:
        resp_msg += '\n\nНа улице тепло'

    await message.answer(resp_msg)

# echo бот повторяет что ему напишем
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# run long-polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
