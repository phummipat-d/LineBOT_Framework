#ไฟล์นี้จะใช้ข้อมูลการแสดงผลจากไฟล์ QuickButtonsItems.py
#สามารถปรับแก้ฟังก์ชัน ReplyQuickButtons เพื่อส่งค่าไปยังฟังก์ชัน getButtonsItems ในไฟล์ QuickButtonsItems.py ได้

from linebot.models import *
from linebot.exceptions import *
from custom.Config import *
import json
import requests
from custom.QuickButtonsItems import getButtonsItems

def ReplyQuickButtons(line_bot_api,replyToken,title):
    items = getButtonsItems()
    text_message = TextSendMessage(text=title,
        quick_reply=QuickReply(
            items=items
        )
    )

    line_bot_api.reply_message(replyToken,text_message)
    return 200

def ReplyQuickButtonsByAPI(replyToken):
    LINE_API = LINE_REPLY_API
    Authorization = 'Bearer {}'.format(CHANNEL_ACCESS_TOKEN) 

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
    
    data = {
        "replyToken":replyToken,
        "messages":[
            {
                "type": "text", 
                "text": "Select your favorite food category or send me your location!",
                "quickReply": 
                { 
                    "items": 
                    [
                        {
                            "type": "action", 
                            "imageUrl": "https://example.com/sushi.png",
                            "action": {
                            "type": "message",
                            "label": "Sushi",
                            "text": "Sushi"
                            }
                        },
                        {
                            "type": "action",
                            "imageUrl": "https://example.com/tempura.png",
                            "action": {
                            "type": "message",
                            "label": "Tempura",
                            "text": "Tempura"
                            }
                        },
                        {
                            "type": "action", 
                            "action": {
                            "type": "location",
                            "label": "Send location"
                            }
                        }
                    ]
                }
            }
        ]
    }
    
    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200
