



import requests
import datetime
import time
import asyncio

from multiprocessing import Process


async def time_m():
    while 1>0:

        await asyncio.sleep(15)
        response = requests.get('http://127.0.0.1:5000/')
        json_response = response.json()
        #repository = json_response['datetime']
        print(json_response[:])
    
 
    
import psutil
async def cpuusage():
    while 1>0:
        await asyncio.sleep(1)
        response = requests.get('http://127.0.0.1:5000/cpuusage')
        json_response = response.json()
        #repository = json_response['datetime']
        print(json_response[:])




#promise all
async def main():
    await asyncio.gather(*[cpuusage(),time_m()])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()