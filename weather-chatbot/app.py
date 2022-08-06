# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:07:02 2019

@author: Spikee
"""

from flask import Flask, request as req
import sys
from witIntegration import wit_response
import Sensor as sen
from pymessenger import Bot
import random

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
PAGE_ACCESS_TOKEN = '*******'# paste your page access token here>"
VERIFY_TOKEN='***' #Any Random String of your Choice 
   
bot = Bot(PAGE_ACCESS_TOKEN)

greeting_responses=['Hi','Hey','*nods*','Hi there','Hello','I am glad! You are talking to me.']
emoji= ['\U0001F642', '\U0001F607', '\U0001F929', '\U0001F643', '\U0001F609']


@app.route("/", methods=['GET'])
def listen():
    if req.args.get("hub.mode") == 'subscribe' and req.args.get('hub.challenge'):
       if not req.args.get('hub.verify_token') == VERIFY_TOKEN:
           return 'Mismatch', 403
       return req.args.get("hub.challenge")
    else:
        return "hello world", 200


def log(message):
    print(message)
    sys.stdout.flush()

def greeting():
    return random.choice(greeting_responses)
       
 
@app.route("/", methods=['POST'])
def webhook():

    data =req.get_json()
    log(data)
    
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                
                #ID's
                sender_id = messaging_event['sender']['id']
                
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    
                    else:
                        messaging_text = 'no text' 
                    
                    #Echo
                    response = ""
                    
                    entity =wit_response(messaging_text)
                    count=0
                    length=len(entity)
                    
                    if 'greet' in entity:
                        response+= greeting()+"\n"
                    
                    if 'alvida' in entity:
                        response+= 'BYE'
                    
                    if 'ok' in entity:
                        response+= random.choice(emoji)
                    
                    if length > 1:
                        response+= "Sure, "
                        
                        for item in entity:
                            
                            if item == 'temp':
                                response += sen.getTemp()+"C"
                                count+=1
                                
                            elif item == 'hum':
                                response += sen.getHum()+"%"
                                count+=1
                                
                            elif item == 'greet' or item == 'ok':
                                count+=1     
                                continue
                            
                            
                            if count != length:
                                response+=", "
                            else:
                                response+="."
                        
                    
                    else:
                        if 'temp' in entity:
                            response += "Sure, "+sen.getTemp()+"C."
                                                        
                        elif 'hum' in entity:
                            response += "Sure, " +sen.getHum()+"%."
                        
                        elif 'greet' in entity:
                            log('greeted')
                        
                        elif 'alvida' in entity:
                            log('greeted')
                        elif 'ok' in entity:
                            log('greeted')
                                
                        else :
                            response= "Sorry, I didn't Understand!!"
                        
                    log(response)
                    bot.send_text_message(sender_id, response)
                    
                
    return "ok", 200



if __name__ == '__main__':
   app.run(host= '0.0.0.0', debug= True)
   