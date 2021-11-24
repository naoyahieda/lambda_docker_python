import requests
import json

expo_push_url = "https://exp.host/--/api/v2/push/send"

push_token = "ExponentPushToken[9e_gS5IRxODynpC9SfJxHx]"

payload = {
    "to": push_token,
    "title":"タイトル！！！！！！", 
    "body": "AWS Lambdaより送信"
  }

def send_push():
    res = requests.post(
            expo_push_url,
            json.dumps(payload),
            headers={'Content-Type': 'application/json'})
    print(res.text)