import json
import requests
import base64
#import time

        
        

def __utc__():
    time_string=[]
    colon = ':'
    for x in obj['when']:
        if x not in colon:
            time_string.append(x)
    obj['when']= ''.join(time_string)

def __processdata__():
                 get_json_from_anpr = requests.get('http://85.236.147.11:8083/api/geniecctv/ANPR?limit=5&after='+str(last_event))
                 s =str
                 data = json.loads(get_json_from_anpr.text)
                 dL = 0
                 dLl = []
                 for x in data:
                     dLi.append(dL)
                     dL = dL+1
                 for Dic in dLi:
                     obj = data[Dic]
                     if obj['direction']== 'toward':
                         obj['direction'] = '1'
                         __utc__()
                     elif obj['direction']=='away':
                         obj['direction'] =='0'
                         __utc__()
                     elif obj['direction']=='stationary':
                         obj['direction']=='3'
                         __utc__()

                     decimgo  = base64.b64decode(obj['plateImageB64'])
                     pimgo = 'overview'+s(obj['plate'])+s(obj['when'])+s(obj['eventId'])+'.jpg'
                     with open(pimgo, 'wb') as f:
                         f.write(decimgo)
                               
                     decimgpch = base64.b64decode(obj['plateImageB64'])
                     pimgpch = 'patch'+s(obj['plate'])+s(obj['when'])+s(obj['eventId'])+'.jpg'
                     with open(decimgpch, 'wb') as f:
                         f.write(decimgpch)

                     decimgplt = base64.b64decode(d['plateImageB64'])
                     plate = 'plate'+s(obj['plate'])+s(obj['when'])+s(obj['eventId'])+'.jpg'
                     with open(decimgplt, 'wb') as f:
                         f.write(decimgplt)
                     
                     rex = 'C:\rex'
                     File = open('rex.csv', 'r+')
                     File.write(s(d['cameraID']+','+s(obj['direction']+','+s(obj['plate'])+','+s(obj['when'][0:10],s(obj['when'][11:23]+','+s(obj['confidence'])+','+rex+pimgo+','+
                                                                                               
                     iD = open('eventId.txt', 'r+')
                     iD.write(s(obj['eventId'])+'\n')
                     last_event  = int(obj['eventId'])                                                                                             
                     iD.close()









last_event = 0
Event_ID_List = []
Event_ID_File = open('eventId.txt')
for eventID in Event_ID_File:
                Event_ID_List.append(event)
Event_ID_File.close()

while True:
        
        #####Needs sorting or when script restarts all events from 1 will be re-processed######
        Event_ID_File = open('eventId.txt')                                                                                                            
        For ID in Event_ID_File:
                if ID not in Event_ID_List:
                        Event_ID_List.append(ID)
        Event_ID_File.close()
        last_event = max(Event_ID_List)                                            
        #######################################################################################         
        
        while True:
                try:
                        x = requests.get('http://85.236.147.11:8083/api/geniecctv/ANPR?limit=5&after='+ last_event)
                        if str(x) == '<Response [200]>':
                                if type(json.loads(x.text))== unicode:
                                        break
                                elif type(json.loads(x.text))== list:
                                        print 'new plate'
                                        __process_data__()
                                         
                        if str(x) == '<Response [404]>':
                                break
                        
                except:
                        break
                


