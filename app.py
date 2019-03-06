# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:07:02 2019

@author: Spikee
"""


#https://privacypolicies.com/privacy/view/62250556b849b30c64e2dc77758e50f1

from flask import Flask, request as req
import os, sys
from witIntegration import wit_response
import Sensor as sen
from pymessenger import Bot

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
PAGE_ACCESS_TOKEN = 'EAAFiW7LUD7MBAAh3iYYz3WzvMMOryCVUtsB0BZAzgySIZCARQq4Nbd9gYQ1OQZAq65BofDyvFgaQyWfPydz5tLVKao29qpoWCFjeZClUokWJ7pZCDMgnPoVUMheJKchAzgG9zH1DCkHi5RAZBQ2kNT3s5hW4xFcmZCYfpfmEfdzquFNcWOo9UgH'# paste your page access token here>"
   
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route("/", methods=['GET'])
def listen():
    if req.args.get("hub.mode") == 'subscribe' and req.args.get('hub.challenge'):
       if not req.args.get('hub.verify_token') =='hello_chat':
           return 'Mismatch', 403
       return req.args.get("hub.challenge")
    else:
        return "hello world", 200

def log(message):
    print(message)
    sys.stdout.flush()
    
@app.route("/", methods=['POST'])
def webhook():

    data =req.get_json()
    log(data)
    
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                
                #ID's
                sender_id = messaging_event['sender']['id']
                recipient_id =  messaging_event['recipient']['id']
                
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    
                    else:
                        messaging_text = 'no text' 
                    
                    #Echo
                    response = ""
                    
                    messaging_text="Temperature, Humidity"
                    entity =wit_response(messaging_text)
                    
                    if len(entity[0])>2:
                        response = "Sure, "
                        for item in entity:
                            
                            if item == 'temp':
                                response += sen.getTemp()
                                log(response)
                            
                            elif item == 'hum':
                                response += sen.getHum()
                                log(response)
                            response+=", "
                        
                    
                    else:
                        if entity[0] == 'temp':
                            response += sen.getTemp()
                            log(response)
                            
                        elif entity[0] == 'hum':
                            response += sen.getHum()
                            log(response)
                                
                        elif entity[0] == "":
                            response= "Sorry, I didn't Understand!!"
    
                    bot.send_text_message(sender_id, response)
                    
                
    return "ok", 200



if __name__ == '__main__':
   app.run(host= '0.0.0.0', debug= True)
   