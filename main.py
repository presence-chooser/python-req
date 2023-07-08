import requests



def time():
    response = requests.get('http://127.0.0.1:5000/')
    json_response = response.json()
    #repository = json_response['datetime']
    print(json_response[:])
    
 
    
import psutil
def cpuusage():
    response = requests.get('http://127.0.0.1:5000/cpuusage')
    json_response = response.json()
    #repository = json_response['datetime']
    print(json_response[:])
    

while True:
    
    time()
    cpuusage() 
