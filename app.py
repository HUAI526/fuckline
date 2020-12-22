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

line_bot_api = LineBotApi('eS4z9G9LP5MpigySxQnBhnezzk8Fx8SRUY5O+FxCu+vXmSMz14xjDwa3Vpik+LBPpEjK9MyW7vJW3ovYlnZo+thBViN8ZgbYq6EhG4HLcSd/hzsb73UY5eJw32nxSZVBdJYbltsSOlTYWhnimi1sOQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9390e26a32374a3789253a5c72c19c65')


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
    r = '你是在大聲什麼啦！'
    if ['早餐', '晚餐', '中餐' ,'午餐'] in msg:
        r = '吃我屌'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()