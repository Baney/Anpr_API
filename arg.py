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

                     #time_string=[]
                     #colon = ':'
                     #for x in obj['when']:
                      #   if x not in colon:
                       #     time_string.append(x)
                     #obj['when']= ''.join(time_string)
                     
                     if obj['direction']== 'Towards':
                         obj['direction'] = '1'
                        
                     elif obj['direction']=='Away':
                         obj['direction'] ='0'
                         
                     elif obj['direction']=='Stationary':
                         obj['direction']='3'
                         

                     decimgo  = base64.b64decode(obj['overviewImageB64'])
                     pimgo = 'overview'+s(obj['plate'])+s(obj['eventID'])+'.jpg'
                     with open(pimgo, 'wb') as f:
                         f.write(decimgo)
                               
                     decimgpch = base64.b64decode(obj['patchImageB64'])
                     pimgpch = 'patch'+s(obj['plate'])+s(obj['eventID'])+'.jpg'
                     with open(pimgpch, 'wb') as f:
                         f.write(decimgpch)

                     decimgplt = base64.b64decode(obj['plateImageB64'])
                     plate = 'plate'+s(obj['plate'])+s(obj['eventID'])+'.jpg'
                     with open(plate, 'wb') as f:
                         f.write(decimgplt)
                     
                     rex = 'C:\rex'
                     File = open('rex.csv', 'a')
                     File.write(s(obj['cameraID'])+','+s(obj['direction'])+','+s(obj['plate'])+','+s(obj['when'][0:10])+','+s(obj['when'][11:23])+','+s(obj['confidence'])+','+rex+pimgo+'\n')
                                                                                               
                     iD = open('eventId.txt', 'r+')
                     iD.write(s(obj['eventID']))
                     last_event  = int(obj['eventID'])                                                                                             
                     iD.close()




last_event = 0
Event_ID_List = []
Event_ID_File = open('eventId.txt')
for eventID in Event_ID_File:
                Event_ID_List.append(int(eventID))
Event_ID_File.close()
        





while True:
    
    Event_ID_File = open('eventId.txt')                                                                                                            
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
    
    


