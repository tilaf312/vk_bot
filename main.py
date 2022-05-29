import vk_api, json
from vk_api.bot_longpoll import VkBotEventType
import random
import config
from MyVkLongPoll import MyVkLongPoll

vk_token = 'fcb715c9650a3a2475974cc92311a806db5164f661c2825ddd5ca195fcdbacd025c8fe4f5bf116d757e93'

vk_session = vk_api.VkApi(token='be24f0ce5f0f311940b38be0c72b3cddc7b2b87e7387170eb5b708ec7714c2c2aecd4ae788b0fed66210c')
longpoll = MyVkLongPoll(vk_session, 213573882)

vadik_id = 150787369
vage_id = 105746541
my_id = 65001811
sipa_id = 151070805


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    print(event)
    ch_id = event.chat_id
    # если событие - это сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        # если событие - пришло от конкретного юзера
        if event.obj.message['from_id'] == my_id:
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
                if event.obj.message['attachments'][0]['type'] == 'wall':
                    sender(ch_id, random.choice(config.photos_list))
            except IndexError:
                print('Сообщение не является репостом')
        else:
            print('Сообщение не от Вадика')