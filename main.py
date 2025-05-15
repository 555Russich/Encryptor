import logging
import asyncio
import string

from dotenv import get_key

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from my_logging import get_logger


BOT_TOKEN = get_key('.env', 'BOT_TOKEN')
cypher = [('A', 'B'), ('a', 'b'), ('B', 'C'), ('b', 'c'), ('C', 'D'), ('c', 'd')]

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
router = Router()


@router.message(Command('encrypt'))
async def encrypt(message: Message):
    text = message.text.replace('/encrypt ', '')
    enc_text = []
    for s in text:
        for alphabet in (string.ascii_uppercase, string.ascii_lowercase):
            if s in alphabet:
                i = alphabet.index(s)
                print(i, len(alphabet))
                if i < len(alphabet)-1:
                    char = alphabet[i + 1]
                elif i == len(alphabet)-1:
                    char = alphabet[0]
                enc_text.append(char)
                break
        else:
            enc_text.append(s)

    await message.answer(''.join(enc_text))
    await asyncio.sleep(60)
    await message.delete()


@router.message(Command('decrypt'))
async def decrypt(message: Message):
    text = message.text.replace('/decrypt ', '')
    dec_text = []
    for s in text:
        for alphabet in (string.ascii_uppercase, string.ascii_lowercase):
            if s in alphabet:
                i = alphabet.index(s)
                char = alphabet[i-1]
                dec_text.append(char)
                break
        else:
            dec_text.append(s)

    m = await message.answer(''.join(dec_text))
    await asyncio.sleep(60*60*10)
    await m.delete()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    get_logger('encryptor.log')

    # try:
    asyncio.run(main())
    # except Exception as global_error:
    #     logging.error(global_error, exc_info=True)
    #     exit(1)
