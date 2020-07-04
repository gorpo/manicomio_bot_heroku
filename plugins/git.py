import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username, keys
from utils import send_to_dogbin, send_to_hastebin


async def git(msg):
    if msg.get('text'):
        if msg['text'].startswith('/git ') or msg['text'].startswith('!git') or msg['text'].startswith('git'):
            text = msg['text'][5:]
            print('Usuario {} solicitou /git'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /git  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True


        if msg['text'].startswith('/git@gorpo_bot') :
            text = msg['text'][15:]
            print('Usuario {} solicitou /git'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /git  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True