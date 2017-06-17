#########Comment this code ###########

import json
import requests
import base64
#import time


        



def __processdata__(x):
                 get_json_from_anpr = requests.get('http://85.236.147.11:8083/api/geniecctv/ANPR?limit=5&after='+x)
                 s =str
                 data = json.loads(get_json_from_anpr.text)
                 dL = 0
                 dLl = []
                 for x in data:
                     dLl.append(dL)
                     dL = dL+1
                 for Dic in dLl:
                     obj = data[Dic]

                     time_string=[]
                     
                     for x in obj['when']:
                         if x =='-':
                            time_string.append('/')
                         elif x not =='-':
                             time.string.append(x)
                     obj['when']= ''.join(time_string)
                     
                     if obj['direction']== 'Towards':
                         obj['direction'] = '1'
                        
                     elif obj['direction']=='Away':
                         obj['direction'] ='0'
                         
                     elif obj['direction']=='Stationary':
                         obj['direction']='3'
                         

                     decimgo  = base64.b64decode(obj['overviewImageB64'])
                     pimgo = 'C:\REX\IMAGE\'+(obj['plate'])+'_'+s(obj['eventID'])+'_OVW'+'.jpg'
                     with open(pimgo, 'wb') as f:
                         f.write(decimgo)
                               
                     decimgpch = base64.b64decode(obj['patchImageB64'])
                     pimgpch = 'C:\REX\IMAGE\'+s(obj['plate'])+'_'+s(obj['eventID'])+'_PCH'+'.jpg'
                     with open(pimgpch, 'wb') as f:
                         f.write(decimgpch)

                     decimgplt = base64.b64decode(obj['plateImageB64'])
                     plate = 'C:\REX\IMAGE\'+s(obj['plate'])+'_'+s(obj['eventID'])+'_LPR'+'.jpg'
                     with open(plate, 'wb') as f:
                         f.write(decimgplt)
                     
                     rex = 'C:\REX'
                     File = open('C:\REX\REX.csv', 'a')
                     File.write(s(obj['cameraID'])+','+s(obj['direction'])+','+s(obj['confidence'])+','+s(obj['plate'])+','+s(obj['when'][0:10])+','+s(obj['when'][11:23])+','+pimgpch+','+plate+','+pimgo+'\n')
                                                                                               
                     iD = open('C:\REX\eventId.txt', 'r+')
                     iD.write(s(obj['eventID']))
                     last_event  = int(obj['eventID'])                                                                                             
                     iD.close()




last_event = 0
Event_ID_List = []
Event_ID_File = open('C:\REX\eventId.txt')
for eventID in Event_ID_File:
                Event_ID_List.append(int(eventID))
Event_ID_File.close()
        





while True:
    
    Event_ID_File = open('C:\REX\eventId.txt')                                                                                                            
    for ID in Event_ID_File:
            if int(ID) not in Event_ID_List:
                    Event_ID_List.append(int(ID))
    Event_ID_File.close()
    last_event = max(Event_ID_List)
    #print last_event
    
    #######################################################################################         
    
    
    try:
            x = requests.get('http://85.236.147.11:8083/api/geniecctv/ANPR?limit=5&after='+str(last_event))
            if str(x) == '<Response [200]>':
                    if type(json.loads(x.text))== unicode:
                            print 'no new data'
                            
                    elif type(json.loads(x.text))== list:
                            print 'processing data'
                            __processdata__(str(last_event))
                            
                             
            if str(x) == '<Response [404]>':
                    print 'shit is mixed up'
            
    except:
            print ' it all over goodbye!!!'
            print last_event
    
    

