# -*- coding: UTF-8 -*-
#######################
# 更多的阿里钉钉API可以参考https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
#######################
import requests
import json

class DingRobot:
    s = requests.session()
    token = None

    def __init__(self, token):
        self.token = token
        print("token is " + self.token)

    # 发送钉钉消息
    def send_msg(self, dingAlarm):
        url = "https://oapi.dingtalk.com/robot/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": dingAlarm.title,
                "text": dingAlarm.text
            },
            "at": {
                "atMobiles": dingAlarm.atMobiles,
                "isAtAll": dingAlarm.isAtAll
            }
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code == 200:
            return json.loads(rep.content)
        else:
            print("request failed.")
            return None

if __name__ == '__main__':
   pass
