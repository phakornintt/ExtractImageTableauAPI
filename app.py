from flask import Flask, request, abort, send_file
import requests
import json
import config as cfg
import os
from datetime import date

folder_path = os.path.join('static', 'images')
filename = 'Dashboard 10_'+ str(date.today()) +'.png'
file_path = folder_path + '/{}'.format(filename)
endpoint = 'https://0a87-110-77-146-31.ap.ngrok.io' # Change endpoint every restart ngrok

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        print(payload)
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        message = message.lower()
        print(message)
        if 'test' in message.lower():
            Reply_image = f"{endpoint}/static/images/Dashboard%2010_2022-05-23.png"
            Reply_imagePrev = f"{endpoint}/static/images/Dashboard%2010_2022-05-23.png"
            # Reply_image = "./Dashboard 10.png"
            # Reply_imagePrev = "./Dashboard 10.png"
            ReplyImage(Reply_token, Reply_image, Reply_imagePrev, cfg.channelAccTkn)
        else:
            "Didn't have this command yet."
        return request.json, 200
    else:
        abort(400)
def ReplyImage(Reply_token, Reply_image, Reply_imagePrev, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken": Reply_token,
        "messages":[
        {
                "type": "image",
                "originalContentUrl": Reply_image,
                "previewImageUrl": Reply_imagePrev
        }]
    }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[{
        "type":"text",
        "text":TextMessage
        }]
    }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200

def ReplyImageMsg(Reply_token, TextMessage, Reply_image, Reply_imagePrev, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken": Reply_token,
        "messages": [
            {
            "type": "text",
            "text": TextMessage
            },
            {
            "type": "image",
            "originalContentUrl": Reply_image,
            "previewImageUrl": Reply_imagePrev
            }
        ]
    }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200
@app.route('/index')
def dashboard():
    # file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Dashboard 10_2022-05-17.png')
    return f"<body><img src='{file_path}' alt='User Image'/></body>"

if __name__ == '__main__':
    app.run(debug=True)
