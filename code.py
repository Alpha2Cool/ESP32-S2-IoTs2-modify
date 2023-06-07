import time
from hiibot_iots2 import IoTs2
iots2 = IoTs2()
b = -1.0
step = 0.05
while True:
    if abs(b) < 1.1:
        b += step
    else:
        b = -1.0
    iots2.blueLED_bright  =  abs(b)
    time.sleep(0.01)