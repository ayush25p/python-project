import time

seconds = 5

for i in range(seconds):
    print(seconds-i, end='\r')
    time.sleep(1)
    
    
    