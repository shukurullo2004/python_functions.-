import time
myTime = int(input("enter time: "))
for x in range(myTime, 0):
    second = x/60
    time.sleep(4)
    print(x)