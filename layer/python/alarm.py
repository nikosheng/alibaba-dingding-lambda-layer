# -*- coding: UTF-8 -*-

class Alarm:

    def __init__(self, title, text, atMobiles, isAtAll):
        self.title = title               #首屏会话透出的展示内容
        self.text = text                 #markdown格式的消息
        self.atMobiles = atMobiles       #被@人的手机号(在text内容里要有@手机号)
        self.isAtAll = isAtAll           #@所有人时：true，否则为：false

if __name__ == '__main__':
    pass