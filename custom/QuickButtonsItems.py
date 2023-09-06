
def getButtonsItems():
    data = [
        ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png","Sushi","Sushi"],
        ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png","Hamberger","Hamberger"]
    ]

    items = []
    for item in data:
        button = {
            "type": "action", 
            "imageUrl":item[0],
            "action": {
                "type": "message",
                "label": item[1],
                "text": item[2]
            }
        }
        items.append(button)
    
    return items