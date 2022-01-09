from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
import random

line_bot_api = LineBotApi('BKeap2C2/GF12NIzSB7FmL4pX28xE+l2u0MJhUsON5CR2PM1JutNBtZV0bt7VDkSpEjK9MyW7vJW3ovYlnZo+thBViN8ZgbYq6EhG4HLcSdWWO5f2giuwHWosKD9YIm1yTQM45dLNCa4u04pmiyqygdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e505df37bcb1b4c392c7bc12396eb941')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = random.randint(0,30)
    if s == 5:
        r = '閉嘴'
    elif '早餐' in msg:
        r = '幾點哪裡'
    elif '午餐' in msg:
        r = '吃早餐店不叫午餐好不好'
    elif '晚餐' in msg:
        r = '吃我屌'
    elif '宵夜' in msg:
        r = '吃我屌'
    elif '要幹嘛' in msg:
        r = random.choice([
            '做愛', '打球', '健身', '去看女生洗澡', '不知道', '上你', '上課怎麼樣', '約臭妹妹壞壞'])
    elif '出門' in msg:
        r = random.choice(['誒你要確定誒','是不是在騙','最好不要比我晚到'])
    elif '打球' in msg:
        r = random.choice(['不去的都是俗仔','想被電？菜雞'])
    elif '有人在臭' in msg:
        r = '又在臭'
    
        


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()