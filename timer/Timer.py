import time
myTime = int(input("enter time: "))
for x in range(myTime, 0, -1):
    second = x%60
    time.sleep(1)
    print(x)