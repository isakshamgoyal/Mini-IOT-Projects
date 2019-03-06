# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:03:51 2019

@author: Spikee
"""

from wit import Wit

access_token = 'V46DKRYALM77B7FABQUVPFAFO3UGYP3Y'


client = Wit(access_token= access_token)


#def wit_response(message_text):
#    resp =client.message(message_text)  
#    entity = None
#    value = None
#    
#    try:
#        entity= list(resp['entities'])[0]
#        value= resp['entities'][entity][0]['value']
#    
#    except:
#        pass
#    return (entity, value)
def wit_response(message_text):
    resp =client.message(message_text)  
    entity = None
    value = None
    
    try:
        entity= list(resp['entities'])
        #value= resp['entities'][entity][0]['value']
    
    except:
        pass
    return entity
        
print(wit_response('bie'))
