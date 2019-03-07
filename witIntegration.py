# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:03:51 2019

@author: Spikee
"""

from wit import Wit

access_token = 'V46D***'

client = Wit(access_token= access_token)

def wit_response(message_text):
    resp =client.message(message_text)  
    entity = None

    try:
        entity= list(resp['entities'])
          
    except:
        pass
    return entity
        
#print(wit_response('bie'))
