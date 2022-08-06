# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:30:14 2019

@author: Spikee
"""

#Reading Data From ThingSpeak
import urllib.request
import json

READ_API_KEY='0FC8***' #Paste your READ_API_KEY Here
CHANNEL_ID= '71***' #Paste your Channe ID Here

def getValue():
    TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                          % (CHANNEL_ID,READ_API_KEY))
    
    response = TS.read()
    data=json.loads(response)
    
        
    temp = data['field1']
    humidity = data['field2']
    TS.close()
    return (temp, humidity) 

def getTemp():
    temp = getValue() 
    return 'Temperature is '+temp[0]

def getHum():
    hum= getValue()
    return 'Humidity is '+hum[1]
    