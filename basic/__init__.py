from flask import Flask, request, abort,jsonify
from custom.Config import *
from custom.WebhookManager import *

from linebot import (
    LineBotApi, WebhookHandler
)

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route(WEBHOOK_ROOT, methods=['POST'])
def webhook():
    payload = request.json
    manage(line_bot_api,payload)
    return "OK",200

@app.route(IMAGES_ROOT, methods=['POST','GET'])
def images():
    message_id = "None"
    if request.method == 'POST':
        message_id = request.form.get('message_id')
    else:
        message_id = request.args.get('message_id')

    import base64
    encoded_string = "None"
    file_path = "media/{}.png".format(message_id)
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string,200