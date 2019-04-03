import itchat
from itchat.content import *
import requests
import datetime
import time

def get_response(question):

    apikey = '9d19f2f79b0f43ec9406fc8ecdd91dab'
    url = 'http://www.tuling123.com/openapi/api?key=' + apikey + '&info=' + question

    res = requests.get(url).json()

    return res['text']

@itchat.msg_register(TEXT,isFriendChat=True)
def auto_reply(msg):
    # _nickName = msg['User']['NickName']
    # _RemarkName = msg['User']['RemarkName']
    # print(_nickName + ':' + _RemarkName)
    print('消息内容:%s' % msg['Content'])
    itchat.send_msg(get_response(msg['Content']),toUserName=msg['FromUserName'])
    print("auto reply :%s"%(get_response(msg['Content'])))

def get_weather_forcast():

    apikey = 'ffa2e199264d8575ebb6a165a272852c'
    url = 'http://v.juhe.cn/weather/index?format=2&cityname=北京&key=' + apikey
    weather = requests.get(url).json()

    return weather

def get_sentence(url):

    sentence = requests.get(url).json()

    return sentence

if __name__ == '__main__':

    itchat.auto_login(hotReload=True)

    url = 'http://open.iciba.com/dsapi'
    sentence = get_sentence(url)    #每日一句
    weather_forcast = get_weather_forcast() #天气预报
    # temperature = weather_forcast['result']['today']['temperature']
    # weather = weather_forcast['result']['today']['weather']
    # wind = weather_forcast['result']['today']['wind']
    # dressing_index = weather_forcast['result']['today']['dressing_index']
    # dressing_advice = weather_forcast['result']['today']['dressing_advice']

    content = sentence['content'] #英文句子
    note = sentence['note'] #中文翻译

    users = itchat.search_friends("李悦")    #找到用户
    # users = itchat.search_chatrooms("二货欢乐多")
    userName = users[0]['UserName']
    remarkName = users[0]['RemarkName'] #获取好友备注名称

    while 1:

        t = datetime.datetime.now()  # 获取当前时间

        # if t.hour == 18 and t.minute == 22:
        if t.second >1:

            itchat.send(msg = '现在是北京时间：%s'%(datetime.datetime.now()),toUserName=userName)
            # itchat.send(msg = '今天天气：%s\n温度:%s\n风速:%s\n穿衣指数:%s\n穿衣建议:%s'%(weather,temperature,wind,dressing_index,dressing_advice),toUserName=userName)
            itchat.send(msg = '%s:\n%s'%(content,note),toUserName=userName)
            itchat.send(msg = 'send by 最爱你的人（我是你，你是你对象假设）',toUserName=userName)
            itchat.run()

            break
        else:

            time.sleep(1)
            print(t)
            continue

    time.sleep(86400)