import telebot
import random
import emoji
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('TOKEN')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Мотивация😎')
keyboard1.row('Рандомное Bидео Игаря💣')
keyboard1.row('Сгенерировать Тренировку🎲')
keyboard1.row('Случайная Видео Тренировка от Игоря🔥')
keyboard1.row('Музыка Чтобы Круто🎶')
keyboard1.row('Статистика канала🔍')
keyboard1.row('Симулятор качка🥊')
keyboard1.row('Канал Игоря💯')

markup = telebot.types.InlineKeyboardMarkup()
markup.add(telebot.types.InlineKeyboardButton(text='Видео Тренировка от Игоря🔥', callback_data='тренировка'))

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Погнали!')
    answer = VideoTrIgor()
    bot.send_message(call.message.chat.id, answer)

def Motivation():
    cit = ['Те, кто добивается выдающихся результатов, обращают внимание даже на самые незначительные детали. Они чаще принимают мелкие, почти незаметные, но верные бытовые решения. Каждый день. Дело не в таланте, просто однажды они решили поступать именно так. Выбирать нужное.', 
    'Если бы люди поняли, что страхи не имеют никакой связи с реальностью, всем жилось бы куда лучше.', 
    'Главное правило стратегического мышления гласит: чтобы тщательно проанализировать объект, нужно от него дистанцироваться.',
    'Совершенно естественно проиграть в том, чего прежде не делал.',
    'Многие люди терпят неудачу только потому, что сдаются в двух шагах от успеха.',
    'Жизнь никогда не течет линейно. Проблемы неизбежны, вопрос в том, как мы их воспринимаем или с ними справляемся.',
    'Не начав действовать, ты в любом случае потерпишь неудачу.',
    'Если ты выполняешь свои обязанности, то эгоизмом с твоей стороны будет как раз не делать то, что доставляет тебе радость, не реализовывать свой талант.',
    'Подними планку. Делай то, на что ты вроде бы не способен. Не задумывайся о пределе своих возможностей. Делай то, чего сделать не можешь.',
    'Если ты задашь правильный вопрос, то получишь верный ответ.',
    'НОВАЯ идея может быть непонятной, глупой или одновременно глупой и непонятной. Нельзя судить о ней по описанию. Ее нужно воплотить.',
    'Не ошибается тот, кто ничего не делает. Томас Эдисон сказал: «Во всех 200 лампочках, которые не работали, было что-то, что я учел в следующей попытке».',
    'Попав в череду положительных результатов всего одного сдвига в своем поведении, ты встаненешь на путь постоянного саморазвития.',
    'Искусство работы над собой строится не вокруг идеала, а вокруг приоритетов. Их надо правильно взвешивать и расставлять, чтобы добиться успеха, тогда они будут меняться вместе с тобой.',
    'Бездействие порождает беспокойство и страх. Действие — уверенность и смелость. Если ты хочешь победить страх, не сиди дома и не думай об этом. Встань и действуй.',
    'Существует всего один способ прожить жизнь счастливо: заниматься тем, что не только интересно, но и имеет смысл.',
    'Знание — это не навык. Навык — это знание плюс 10 000 повторений.',
    'Если ты не знаешь, чего хочешь, ты в итоге останешься с тем, чего точно не хочешь.',
    'Чтобы дойти до цели, надо идти.',
    'Волк - это не робота. Ворк - работа, а волк - это ходить.',
    'Лучше быть последним-первым, чем первым-последним.',
    'Не важно кто важно кто.',
    'Кровь у тебя в крови.',
    'Не слушай тех, кто много обещают, они обычно, много обещают.',
    'Настоящий отец - мать, брат, трюродный дед.',
    'Сильный не тот, кто сильный, а тот, кто сильный.']
    result = random.choice(cit)
    return result

def VideoIgor():
    with open('videos.txt', 'rb') as f:
        f = random.choice(list(open('videos.txt')))
        return f

def VideoTrIgor():
    with open('TRvideos.txt', 'rb') as f:
        f = random.choice(list(open('TRvideos.txt')))
        return f

#Ген. трени
def PushUps():
    Push = ['10', '15', '20', '30', '40', '50']
    Reps = ['1', '2', '3', '4']
    pRan = random.choice(Push)
    Rran = random.choice(Reps)
    result = 'Грудь.\nОтжимания - {0} раз, по {1} подхода\n'.format(pRan, Rran)
    if (Rran == '1'):
        return 'Грудь.\nОтжимания - {0} раз, {1} подход\n'.format(pRan, Rran)
    return result

def Should():
    Style = ['Армейские отжимания 120°', 'Армейские отжимания 90°', 'Отжимания на руках у стены']
    Count = ['5', '10', '15', '20']
    Reps = ['1', '2', '3', '4']
    sRan = random.choice(Style)
    cRan = random.choice(Count)
    Rran = random.choice(Reps)
    result = 'Плечи.\n{0} - {1} раз, по {2} подхода\n'.format(sRan, cRan, Rran)
    if (Rran == '1'):
        return 'Плечи.\n{0} - {1} раз, {2} подход\n'.format(sRan, cRan, Rran)
    return result

def Triceps():
    Style = ['Дракон', 'Отжимания треугольник', 'Отжимания у скамьи']
    Count = ['10', '15', '20', '30', '40', '50']
    Reps = ['1', '2', '3', '4']
    sRan = random.choice(Style)
    cRan = random.choice(Count)
    Rran = random.choice(Reps)
    result = 'Трицепс.\n{0} - {1} раз, по {2} подхода\n'.format(sRan, cRan, Rran)
    if (Rran == '1'):
        return 'Трицепс.\n{0} - {1} раз, {2} подход\n'.format(sRan, cRan, Rran)
    return result

def Press():
    Style = ['Велосипед', 'Подъем ног', 'Подъемы ног с тазом', 'Ножницы', 'Планка']
    Plank = ['1 мин.', '1:30 мин.', '2 мин.', '2:30 мин.','3 мин.', '3:30 мин.', '4 мин.', '4:30 мин.', '5 мин.']
    Count = ['10', '15', '20', '30', '40', '50']
    Reps = ['1', '2', '3', '4']
    pRan = random.choice(Plank)
    sRan = random.choice(Style)
    cRan = random.choice(Count)
    Rran = random.choice(Reps)
    result = 'Пресс.\n{0} - {1} раз, по {2} подхода\n'.format(sRan, cRan, Rran)
    if (Rran == '1'):
        return 'Пресс.\n{0} - {1} раз, {2} подход\n'.format(sRan, cRan, Rran)
    elif (sRan == 'Планка'):
        return 'Пресс.\n{0}, {1}\n'.format(sRan, pRan)
    elif (sRan == 'Планка' and Rran == '1'):
        return 'Пресс.\n{0}, {1}\n'.format(sRan, pRan)
    return result

def Legs():
    Style = ['Пистолетик', 'Болгарские приседания', 'Пистолетик с опорой', 'Мост со стула с двух ног']
    StyleTwo = ['Выпрыгивания', 'Выпрыгивания с поднятием коленей', 'Подъемы голени на одной ноге']
    Count = ['5', '10', '12', '15']
    TCount = ['10', '15', '20', '25', '30', '35', '40', '50']
    Reps = ['1', '2', '3', '4']
    stRan = random.choice(StyleTwo)
    ctRan = random.choice(TCount)
    rtRan = random.choice(Reps)
    sRan = random.choice(Style)
    cRan = random.choice(Count)
    Rran = random.choice(Reps)
    result = 'Ноги.\n{0} - {1} раз, по {2} подхода.\n{3} - {4} раз, по {5} подхода'.format(sRan, cRan, Rran, stRan, ctRan, rtRan)
    if (Rran == '1'):
        return 'Ноги.\n{0} - {1} раз, {2} подход.\n{3} - {4} раз, по {5} подхода'.format(sRan, cRan, Rran, stRan, ctRan, rtRan)
    elif (Rran == '1' and rtRan == '1'):
        return 'Ноги.\n{0} - {1} раз, {2} подход.\n{3} - {4} раз, {5} подход'.format(sRan, cRan, Rran, stRan, ctRan, rtRan)
    elif (rtRan == '1'):
        return 'Ноги.\n{0} - {1} раз, по {2} подхода.\n{3} - {4} раз, {5} подход'.format(sRan, cRan, Rran, stRan, ctRan, rtRan)
    return result

def Card():
    Style = ['Берпи без отжимания и прыжка', 'Берпи без прыжка', 'Берпи', 'Берпи с поднятием коленей в прыжке', 'Берпи и "Скалолаз"', 'Берпи с прыжками Джампинг Джек', 'Берпи с поворотом на 180°']
    Count = ['10', '15', '20', '30', '40', '50']
    Reps = ['1', '2', '3', '4']
    sRan = random.choice(Style)
    cRan = random.choice(Count)
    Rran = random.choice(Reps)
    result = 'Кардио.\n{0} - {1} раз, по {2} подхода\n'.format(sRan, cRan, Rran)
    if (Rran == '1'):
        return 'Кардио.\n{0} - {1} раз, {2} подход\n'.format(sRan, cRan, Rran)
    return result

#Агрится на частое нажатие "Мотивация"
i_mot = ['0']
def Angry():
    return i_mot.append('0')

#Парсер стат. с сайта
def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'     
    return r.text

def get_head(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('table', class_='table').find_all('b')
    heads = []
    for i in head:
       heads.append(i.string)
    return heads 

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здарова брат, готов визуализировать вместе со мной и работать вхламину?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Отлично, дружище! Выбери то, что тебя интересует и поехали!', reply_markup=keyboard1)
    elif message.text.lower() == 'нет':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBE2lfFZ9M4T7PxyLwAAHLwTy0te4sHU8AAkABAAKoISEGLFI-ZqIj4G4aBA')
    elif 'мотивация' in message.text.lower():
        Angry()
        if (len(i_mot) == 15):
            bot.send_photo(message.chat.id, open('/image/111.jpg', 'rb'))
        elif (len(i_mot) == 20):
            bot.send_photo(message.chat.id, open('/image/222.jpg', 'rb'))
        elif (len(i_mot) == 25):
            bot.send_photo(message.chat.id, open('/image/333.jpg', 'rb'))
        elif (len(i_mot) > 30):
            bot.send_photo(message.chat.id, open('/image/444.jpg', 'rb'))
        else:
            bot.send_message(message.chat.id, Motivation())
    elif 'канал игоря' in message.text.lower():
        bot.send_message(message.chat.id, 'Заходи ежжи, мне очень нужна твоя поддержка, братан. Топим, визуализируем здесь 👉 https://www.youtube.com/channel/UC7DFMwmTVwwSO2E5vs2GgQw')
        bot.send_photo(message.chat.id, open('E:/Sublime Text 3/Projects/BotPy/image/555.png', 'rb'))
    elif 'игаря' in message.text.lower():
        bot.send_message(message.chat.id, VideoIgor())
    elif 'сгенерировать тренировку' in message.text.lower():
        bot.send_message(message.chat.id, 'Твоя тренировка на сегодня!💥\n---------------------------------------------------------------------\n{0}\n---------------------------------------------------------------------\n{1}\n---------------------------------------------------------------------\n{2}\n---------------------------------------------------------------------\n{3}\n---------------------------------------------------------------------\n{4}\n---------------------------------------------------------------------\n{5}\n---------------------------------------------------------------------\n Отдых перед подходом 1:30 - 2:00 минуты\nЕсли не знаешь какое-то упражнение, просто вводи команду /search'.format(PushUps(), Should(), Triceps(), Press(), Legs(), Card()))
        bot.send_message(message.chat.id, 'Или выполни случайную тренировку с канала👇', reply_markup=markup)
    elif message.text.lower() == '/search':
        bot.send_message(message.chat.id, 'Выйди из зоны комфорта, брат, и гугли сам, потому что да ежжи💪')
    elif 'видео тренировка от игоря' in message.text.lower():
        bot.send_message(message.chat.id, VideoTrIgor())
    elif 'музыка' in message.text.lower():
            musics = ['/musics/NEFFEX - Fight Back.mp3', 
            '/musics/NEFFEX - Never Give Up.mp3',
            '/musics/NEFFEX - Best of Me.mp3',
            '/musics/Neffex - Crown.mp3',
            '/musics/NEFFEX - Dance Again.mp3',
            '/musics/Neffex - Failure.mp3',
            '/musics/NEFFEX - Graveyard.mp3',
            '/musics/NEFFEX - Greatest.mp3',
            '/musics/NEFFEX - Play.mp3',
            '/musics/Neffex - Rumors.mp3',
            '/musics/NEFFEX - Soldier.mp3',
            '/musics/NEFFEX - Things Are Gonna Get Better.mp3',
            '/musics/NEFFEX - Unstoppable.mp3',
            '/musics/Rick-Astley-Never-Gonna-Give-You-Up.mp3']
            r = random.choice(musics)
            bot.send_document(message.chat.id, open(r, 'rb'))
    elif 'статистика' in message.text.lower():
        res = get_head(get_html('https://whatstat.ru/channel/UC7DFMwmTVwwSO2E5vs2GgQw'))
        bot.send_message(message.chat.id, 'Подписчики - {0} 📈\nПросмотры - {1} 👀\nВидео - {2} 📹\nСтатистика обновляется ежедневно'.format(res[0], res[1], res[2]))
    elif 'симулятор' in message.text.lower():
        bot.send_message(message.chat.id, 'Вперёд, качалка специально для тех, кто хочет прогрессировать💪 (Или кому просто лень)\nshorturl.at/ILU27')
    else:
        bot.send_message(message.chat.id, 'Не понял тебя, брат')
#
bot.polling(none_stop=True)