import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from datetime import *
from time import sleep

id=[]
vk_session = vk_api.VkApi(token='c0c0d93cad375077e8ea8178d5f075ddd838371501f5e9c8df25b9ec2b3434e312c4229d3f5081fb94c29')
longpoll = VkBotLongPoll(vk_session, 199644098)
vk = vk_session.get_api()
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if '/start' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key=('140a8fd760ef998de095bf1b9c92b822201366a2'),
                    server=('https://lp.vk.com/wh199644098'),
                    ts=('3'),
                    random_id=get_random_id(),
                    message='Привет! Я буду присылать уведомления об уроках за 5 минут до их начала и ссылку на урок. Даже если МЭШ будет лежать, я пришлю ссылку на урок. Вот такой вот я молодец.',
                    chat_id=event.chat_id
                )
                id.append(event.chat_id)
                break

# dnevnik.mos.ru/conference/?scheduled_lesson_id=
#
# 33 часа


# 2 физики:
# 197629115   197631242   203745172   197633585          Разность 2127
# 197629116   197631243   203745173   197633586
fiz=197631242
fizc=0
fizm=2
# 5 инф:
# 197629117   197631244
# 197629119   197631245          118 отсутствует
# 197629120   197631246
# 197629121   197631247
# 197629122   197631248
inf=197631244
infc=0
infm=5
# 2 геометрии:
# 197629123   197631249
# 197629124   197631250
geom=197631249
geomc=0
geomm=2
# 2 физры:
# 197629125   197631251
# 197629126   197631252
fra=197631251
frac=0
fram=2
# 6 матеш:
# 197629127   197631253
# 197629128   197631254
# 197629129   197631255
# 197629130   197631256
# 197629131   197631257
# 197629132   197631258
alg=197631253
algc=0
algm=6
# 3 литры:
# 197629133   197631259
# 197629134   197631260
# 197629135   197631261
lit=197631259
litc=0
litm=3
# 2 истории:
# 197629136   197631262
# 197629137   197631263
ist=197631262
istc=0
istm=2
# 1 общество:
# 197629138   197631264
obs=197631264
obsc=0
obsm=1
# 2 географии:
# 197629139   197631265
# 197629140   197631266
geog=197631265
geogc=0
geogm=2
# 3 инглиша:
# 197629141   197631267
# 197629142   197631268
# 197629143   197631269
eng=197631267
engc=0
engm=3
# 1 биология:
# 197629144   197631270
bio=197631270
bioc=0
biom=1
# 1 русский:
# 197629145   197631271
rus=197631271
rusc=0
rusm=1
# 1 химия:
# 197629146   197631272   203745198
him=197631272
himc=1
himm=0
# 2 обж:
# 197631273   197629147
# 197631274   197629148
obj=197629147
objc=0
objm=2

fiz-=1
geom-=1
inf-=1
fra-=1
alg-=1
lit-=1
ist-=1
obs-=1
geog-=1
eng-=1
bio-=1
him-=1
obj-=1

pn=['alg','alg','inf','obs','lit','lit']
vt=['geog','geog','ist','ist','inf','fra','eng']
sr=['alg','alg','obj','obj','inf','inf']
ct=['geom','geom','him','bio','fiz','eng','inf']
pt=['fiz','alg','lit','alg','rus','eng','fra']
nedel=[pn,vt,sr,ct,pt,[],[]]

uroki=["5:55:00","6:55:00","7:55:00","8:55:00","9:55:00","10:55:00","11:55:00"]


# print(str(timenow)[0:-7])
# print(nedel[weekdaynow])


while True:
    weekdaynow = int(datetime.weekday(datetime.today()))
    timenow = str(datetime.time(datetime.today()))[0:-7]
    print(timenow,weekdaynow)
    if timenow in uroki:
        sleep(1)
        if uroki.index(timenow)>=len(nedel[weekdaynow]):
            continue
        urok=nedel[weekdaynow][uroki.index(timenow)]
        if urok=="alg":
            urokname="алгебры"
            algc+=1
            alg+=1
            urokid=alg
        elif urok=="fiz":
            urokname="физики"
            fizc+=1
            fiz+=1
            urokid=fiz
        elif urok=="inf":
            urokname="информатики"
            infc+=1
            inf+=1
            urokid=inf
        elif urok=="geom":
            urokname="геометрии"
            geomc+=1
            geom+=1
            urokid=geom
        elif urok=="fra":
            urokname="физкультуры"
            frac+=1
            fra+=1
            urokid=fra
        elif urok=="lit":
            urokname="литературы"
            litc+=1
            lit+=1
            urokid=lit
        elif urok=="ist":
            urokname="истории"
            istc+=1
            ist+=1
            urokid=ist
        elif urok=="obs":
            urokname="обществознания"
            obsc+=1
            obs+=1
            urokid=obs
        elif urok=="geog":
            urokname="географии"
            geogc+=1
            geog+=1
            urokid=geog
        elif urok=="eng":
            urokname="английского языка"
            engc+=1
            eng+=1
            urokid=eng
        elif urok=="bio":
            urokname="биологии"
            bioc+=1
            bio+=1
            urokid=bio
        elif urok=="rus":
            urokname="русского языка"
            rusc+=1
            rus+=1
            urokid=rus
        elif urok=="him":
            urokname="химии"
            himc+=1
            him+=1
            urokid=him
        elif urok=="obj":
            urokname="ОБЖ"
            objc+=1
            obj+=1
            urokid=obj
        message=str("Через 5 минут начнется урок "+str(urokname)+"\nСсылка: https://dnevnik.mos.ru/conference/?scheduled_lesson_id="+str(urokid))
        for k in id:
            vk.messages.send(
                key=('140a8fd760ef998de095bf1b9c92b822201366a2'),
                server=('https://lp.vk.com/wh199644098'),
                ts=('3'),
                random_id=get_random_id(),
                message=message,
                chat_id=k
            )









# for event in longpoll.listen():
#     if event.type == VkBotEventType.MESSAGE_NEW:
#         if '/start' in str(event):
#             if event.from_chat:
#                 for k in range(5):
#                     vk.messages.send(
#                         key=('140a8fd760ef998de095bf1b9c92b822201366a2'),
#                         server=('https://lp.vk.com/wh199644098'),
#                         ts=('3'),
#                         random_id=get_random_id(),
#                         message='Привет!',
#                         chat_id=event.chat_id
#                     )
# while True:
