# alibaba-dingding-lambda-layer-sam

### Deploy in Serverless Application Repository


- Login AWS Console and navigate to `Serverless Application Repository` service.
- Search `alibaba-dingding-lambda-layer` in `Available Applications`
- Press `Deploy` button to deploy the lambda layer to your account
- Navigate to `Lambda` service and find out the layer is already deployed or not


### Usage

**Please configure the Ali Dingding Robot to invoke the alarm message, for more information about the configuration, please refer to [LINK](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)**

**使用阿里钉钉告警需要提前配置自定义机器人，具体可以参考[阿里官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)**

**Please Make Sure to Input Dingding Robot Access Token in Lambda Evironment Variables**

**使用该Lambda Layer 请务必设置调用Lambda内阿里钉钉机器人Webhook内的Access Token环境变量以调用接口**

```
import json
import os
from layer.dingding import DingRobot
from layer.alarm import Alarm

def hello(event, context):
    token = os.environ['ACCESSTOKEN']
    robot = DingRobot(token)
    dingAlarm = Alarm(
        title = "AWS 告警信息",
        text = "### {0}\n >{1}".format(event['Records'][0]['Sns']['Subject'], event['Records'][0]['Sns']['Message']),
        atMobiles = "",
        isAtAll = True
    )
    body = robot.send_msg(dingAlarm)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

```



Happy Building!  
Niko (nikosheng@gmail.com)