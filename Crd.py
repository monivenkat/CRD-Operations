import threading 
import time
d={}
def create(key,value,timeout=0):
    if key in d:
        print("Error: key already exists")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Error: Memory limit exceeded")
        else:
            print("Error: Invalind keyname")
def read(key):
    if key not in d:
        print("Error: key does not exist") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("Error: time-to-live ",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri
def delete(key):
    if key not in d:
        print("Error: key does not exist ") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print(" successfully deleted")
            else:
                print("error: time-to-live ",key,"has expired") 
        else:
            del d[key]
            print("successfully deleted")
