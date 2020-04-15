from eliza import Eliza
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)
import os
from flask import Flask, request, abort
from dotenv import load_dotenv
load_dotenv()


eliza = Eliza(lang='id')
app = Flask(__name__)

# get LINE_CHANNEL_ACCESS_TOKEN from your environment variable
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
# get LINE_CHANNEL_SECRET from your environment variable
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))


@app.route("/")
def home():
    return "henlo world"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    payload = TextSendMessage(text=eliza.respond(event.message.text))
    if event.message.text.lower()=='p':
        payload = ImageSendMessage(
            original_content_url='https://raw.githubusercontent.com/raisoturu/eliza-line-chatbot/master/assets/images/p.jpg',
            preview_image_url='https://raw.githubusercontent.com/raisoturu/eliza-line-chatbot/master/assets/images/p.jpg'
        )

    line_bot_api.reply_message(event.reply_token,payload)
    


if __name__ == "__main__":
    app.run()
