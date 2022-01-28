import json

import requests

expo_push_url = "https://exp.host/--/api/v2/push/send"

push_token = "ExponentPushToken[sZzGoFEyNF8eF8G-f2_Hoy]"

payload = {
    "to": push_token,
    "title": "タイトル！！！！！！",
    "body": "AWS Lambdaより送信"
}


def send_push():
    res = requests.post(
        expo_push_url,
        json.dumps(payload),
        headers={'Content-Type': 'application/json'})
    print(res.text)
