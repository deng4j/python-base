import json

import requests

"""
使用微信开发者平台测试号，对用户发送信息
"""

# 1. 获取access_token接口
# https请求方式: GET
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

app_id = 'wx6cdxxxx'
app_secret = 'a033xxxxxx'
url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'

resp_json = requests.get(url).json()
print(resp_json)
access_token = resp_json.get('access_token')

# 2. 客服接口 - 发消息
# http请求方式: POST
# https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN

url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}'
opend_id = "oG49O5g0A0PtB7Emxxxxxxxx"
req_data = {
    "touser": opend_id,
    "msgtype": "text",
    "text":
        {
            "content": "您好，我给您发消息了！"
        }
}
response = requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))
print(response.text)
