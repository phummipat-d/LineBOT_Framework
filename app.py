from basic import app
from custom.Config import *
from basic.WebhookUpdater import updateWebHook

if __name__ == "__main__":
    if NGROK_MODE:
        updateWebHook()
        
    app.run(port=PORT)