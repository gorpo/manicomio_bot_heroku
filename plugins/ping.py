
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin
from datetime import datetime


async def ping(msg):
    if msg.get('text'):
        if msg['text'] == 'ping' or msg['text'] == '/ping' or msg['text'] == '/ping@' + bot_username:
            print('Usuario {} solicitou /ping'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /ping  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            first = datetime.now()
            sent = await bot.sendMessage(msg['chat']['id'], '*Pong,kkkjj ai seu ping!*', 'Markdown',
                                         reply_to_message_id=msg['message_id'])
            second = datetime.now()
            await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                      '*Pong!* `{}`ms'.format((second - first).microseconds / 1000), 'Markdown')
            return True

        elif msg['text'] == 'king' or msg['text'] == '!king' or msg['text'] == '/king@' + bot_username:
            await bot.sendMessage(msg['chat']['id'], '*Kong!*', 'Markdown', reply_to_message_id=msg['message_id'])
            return True
        