import vk_api, json
from vk_api.bot_longpoll import VkBotEventType
import random
import config
from MyVkLongPoll import MyVkLongPoll

vk_session = vk_api.VkApi(token=config.vk_token)
longpoll = MyVkLongPoll(vk_session, 213573882)
abc = 'Привет. как дела, все хорошо'

# TODO подумать над структурой

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    print(event)
    ch_id = event.chat_id
    # если событие - это сообщение и пришло от конкретного юзера
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['from_id'] == config.vadik_id:
        # если событие - это фотография
        try:
            if event.obj.message['attachments'][0]['type'] == 'photo':
                sender(ch_id, random.choice(config.photos_list))
        except IndexError:
            print('Сообщение не является фотографией')
        try:
            if event.obj.message['attachments'][0]['type'] == 'audio':
                sender(ch_id, 'Это Мияджи?')
        except IndexError:
            print('Сообщение не является аудио')
            try:
                if event.obj.message['attachments'][0]['type'] == 'video':
                    sender(ch_id, random.choice(config.photos_list))
            except IndexError:
                print('Сообщение не является видео')
        try:
            if event.obj.message['attachments'][0]['type'] == 'wall':
                sender(ch_id, random.choice(config.photos_list))
        except IndexError:
            print('Сообщение не является репостом')
    elif event.type == VkBotEventType.MESSAGE_NEW:
        # TODO подумать как оптимизировать
        text_list = event.obj.message['text'].lower().replace(',', '')
        text_list = text_list.replace('.', '')
        text_list = text_list.replace('!', '')
        text_list = text_list.replace('?', '')
        text_list = text_list.replace('"', '')
        text_list = text_list.split()
        coincidence_weather = None
        coincidence_bot = None
        for word in text_list:
            if word in config.list_name_weather:
                coincidence_weather = True
                break
        for word in text_list:
            if word in config.list_name_bot:
                coincidence_bot = True
                break
        if coincidence_bot and coincidence_weather:
            sender(ch_id, 'запросили погоду')