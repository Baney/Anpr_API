#########Comment this code ###########

import json
import requests
import base64
import time
import os


        



def __processdata__(x):
                 get_json_from_anpr = requests.get('http://127.0.0.1:8083/api/geniecctv/ANPR?limit=5&after='+x)
                 s =str
                 data = json.loads(get_json_from_anpr.text)
                 dL = 0
                 dLl = []
                 for x in data:
                     dLl.append(dL)
                     dL = dL+1
                 for Dic in dLl:
                     obj = data[Dic]
                     
                     
                     time = obj['when'][10:23]
                     rev = obj['when'][0:10]
                     a = rev[0:4]
                     b = rev[5:7]
                     c = rev[8:11]
                     d = '/'
                     rev_date = c+d+b+d+a
                     obj['when']= rev_date+time
                     
                     if obj['direction']== 'Towards':
                         obj['direction'] = '0'
                        
                     elif obj['direction']=='Away':
                         obj['direction'] ='1'
                         
                     elif obj['direction']=='Stationary':
                         obj['direction']='3'

                     
                     whenstr = c+b+a+'\\'
                     

                     if os.access('C:\\REX\\IMAGES\\'+whenstr, os.F_OK) is False:
                         os.makedirs('C:\\REX\\IMAGES\\'+whenstr)

                         
                     
                     folder = 'C:\\REX\\IMAGES\\'+whenstr
                     
                         

                     decimgo  = base64.b64decode(obj['overviewImageB64'])
                     pimgo = folder + s(obj['plate'])+'_'+s(obj['eventID'])+'_OVW'+'.jpg'
                     with open(pimgo, 'wb') as f:
                         f.write(decimgo)
                               
                     decimgpch = base64.b64decode(obj['plateImageB64'])
                     pimgpch = folder + s(obj['plate'])+'_'+s(obj['eventID'])+'_PCH'+'.jpg'
                     with open(pimgpch, 'wb') as f:
                         f.write(decimgpch)

                     decimgplt = base64.b64decode(obj['plateImageB64'])
                     plate = folder + s(obj['plate'])+'_'+s(obj['eventID'])+'_LPR'+'.jpg'
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
    
    
    #######################################################################################         
    
    
    try:
            x = requests.get('http://127.0.0.1:8083/api/geniecctv/ANPR?limit=5&after='+str(last_event))
            if str(x) == '<Response [200]>':
                    if type(json.loads(x.text))== unicode:
                           time.sleep(5)
                           
                           
                            
                    elif type(json.loads(x.text))== list:
                        try:
                            __processdata__(str(last_event))
                            print 'processing data'
                        except:
                            print 'function issue'
                            break
                            
                             
            elif str(x) == '<Response [404]>':
                    print 'Response [404]'
            
    except:
            print ' it all over goodbye!!!'
            print last_event
    
    
