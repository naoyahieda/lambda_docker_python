from utils.send_push_notification import send_push

def handler(event, context):
    send_push()
    print('debug here')
    return 'Hello from AWS Lambda using Python'