import os
import time
import requests

count=0

website=str(input("Please input your target:(bing.com)"))
if(website==""):
    website="bing.com"


interval=input("Please input execute interval:(0.5)")
if(interval==""):
    interval=0.5
else:
    interval=int(interval)

print(end='\n')
print("Httpcheck is testing",website)
print(end='\n')
while  (True):
    back=requests.get("http://"+website)
    count+=1
    print("Code"+str(back.status_code)+" "+back.reason+",test"+str(count),"finish.")
    time.sleep(interval)
    if(count%10==0):
        print(end='\n') 
        print("Httpcheck is testing",website)
        print(end='\n')
#