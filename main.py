import os
import time

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
print("curl2test is testing",website)
print(end='\n')
while  (True):
    os.system("curl "+website)
    count+=1
    #print(end='\n')
    print("Test",count,"finish")
    time.sleep(interval)
    if(count%10==0):
        print(end='\n')
        print("curl2test is testing",website)
        print(end='\n')
#