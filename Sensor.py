# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:30:14 2019

@author: Spikee
"""

#FOR Local Server

#from bs4 import BeautifulSoup
#import urllib3
#import sys
#
#
#base_url = "http://bit.ly/SensorDHT11"
#http=urllib3.PoolManager()
#
#
#
#def getValue():
#    r=http.request('GET',base_url)
#    soup=BeautifulSoup(r.data,'html.parser')
#    a=soup.find_all("h4")
#    print(a[0].text)
#    print(a[1].text)
#    sys.stdout.flush()
#    return 'SureTemperature is '+a[0].text+' and Humidity is '+a[1].text
#    

#Reading Data From ThingSpeak
import urllib.request
import json

READ_API_KEY='0FC8***'
CHANNEL_ID= '71***'

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
    