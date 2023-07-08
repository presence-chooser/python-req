import datetime
import time


def realtime():
    dt = datetime.datetime.now()
    time.sleep(0.5)  
    return str(dt)

def reza():
    df="Post Action"
    return str(df)





# Importing the library
import psutil
def cpuusage():
    cpu_usage=psutil.cpu_percent()
    return str(cpu_usage)
