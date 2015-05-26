import RPi.GPIO as io 

io.setmode(io.BCM) 
doorPin = 17 
io.setup(doorPin, io.IN) 

doorStatusPrev = -1

## Event loop
while True:
    doorStatus = io.input(doorPin)
    if doorStatus != doorStatusPrev:
        if doorStatus:
            print "Open"
        else:
            print "Closed"
    doorStatusPrev = doorStatus
