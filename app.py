from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('6tJTm2THlNyPi4uWFIPYnjEkIv95HPy8UBL8iG37AuACj47CuwoFXrrNlmgt8EkSqxDFr1qilvyj7+ncm0+7daw/7e1e83PA2s8JWcJWGwPwUuk+tZYj4Ed/qcN4AzNUFOJEE/w07f3Odq6Hd/DD+QdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('52e6f871419627ade65793ec90b20474')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
