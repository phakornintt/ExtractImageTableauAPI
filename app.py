from flask import Flask, request, abort
import requests
import json
import config as cfg
import os

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
            Reply_image = "D:\ExtractImageTableauAPI\Dashboard 10.png"
            Reply_imagePrev = "D:\ExtractImageTableauAPI\Dashboard 10.png"
            # Reply_image = "./Dashboard 10.png"
            # Reply_imagePrev = "./Dashboard 10.png"
            ReplyImage(Reply_token, Reply_image, Reply_imagePrev, cfg.channelAccTkn)
        elif 'hello' in message:
            Reply_messasge = 'มีเงาไก่ตามตัว'
            Reply_image = "https://www.img.in.th/images/7687fb1a9765ae5be1169cdd1445f7c2.jpg"
            Reply_imagePrev = "https://www.img.in.th/images/7687fb1a9765ae5be1169cdd1445f7c2.jpg"
            ReplyImageMsg(Reply_token, Reply_messasge, Reply_image, Reply_imagePrev, cfg.channelAccTkn)
            # ReplyImage(Reply_token, Reply_image, Reply_imagePrev, cfg.channelAccTkn)
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

if __name__ == '__main__':
    app.run(debug=True)