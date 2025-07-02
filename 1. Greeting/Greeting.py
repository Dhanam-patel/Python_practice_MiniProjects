import time 
a = time.strftime("%H:%M:%S")
t = int(time.strftime('%H')) 
if(t < 12 and t >= 4):
    print("Good Morning Master")
elif(t < 17 and t >= 12):
    print("Good Afternoon Master")
elif(t <= 22 and t >= 17):
    print("Good Evening Master")