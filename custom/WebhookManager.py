
#ไฟล์นี้จะเป็นไฟล์เริ่มต้นสำหรับการพัฒนาระบบ
#ตัวแปร payload คือข้อมูลที่ถูกส่งมาจากฝั่งผู้ใช้งาน(LineApp)
#การตอบกลับข้อมูลไปให้ผู้ใช้งานฝั้ง LineApp แบบพื้นฐานเช่น ข้อมูล,ภาพ ฯลฯ จะใช้การ Reply ผ่าน basic packages (BasicReplyMessage)
#การตอบกลับข้อมูลไปให้ผู้ใช้งานฝั้ง LineApp ในรูปแบบที่ซับซ้อนมากขึ้น เช่น FlexMessage จะใช้การ Reply ผ่าน custom packages

from custom.Config import *
from basic.BasicReplyMessage import *
from custom.ReplyFlexMessage import ReplyFlexMessage
from custom.QuickReplyButtons import ReplyQuickButtons

def manage(line_bot_api,payload):
    message_type = payload['events'][0]['message']['type']
    replyToken = payload['events'][0]['replyToken']

    #กรณีผู้ใช้งานส่งข้อความเป็น text
    if message_type == "text":
        try:
            #รับข้อความที่ได้จากผู้ใช้งาน
            #txtMessage = payload['events'][0]['message']['text']
            txtMessage = "Hi,your message is : " + payload['events'][0]['message']['text']
            ReplyTextMessage(line_bot_api,replyToken, txtMessage )
        except Exception as e:
            print(e)

    #กรณีผู้ใช้งานส่งข้อความเป็น image
    elif message_type == "image":
        try:
            #ทำกาบันทึกภาพที่ผู้ใช้งานส่งมา
            message_id = payload['events'][0]['message']['id']
            file_path = "media/{}.png".format(message_id)
            message_content = line_bot_api.get_message_content(message_id)
            with open(file_path, 'wb') as fd:
                for chunk in message_content.iter_content():
                    fd.write(chunk)

            #imageURL = "https://etherscan.io/images/ethereum-icon.png"
            #ReplyImageMessage(line_bot_api,replyToken, imageURL,imageURL)

            alt_text = "Tongashi Flex Message"
            ReplyFlexMessage(line_bot_api,replyToken,alt_text)
            #ReplyQuickButtons(line_bot_api,replyToken,"Title QuickButtons")

        except Exception as e:
            print(e) 
    
    return 200