import time as t
import threading


x = 0


def Update():
    global x
    
    #print(x,  currentTime - prevTime)
    x += 1

def mainThread(stop):
    prevTime = 0
    elapsedTime = 0
    count = 0
    
    while True:
        currentTime = t.perf_counter_ns()
        elapsedTime += currentTime - prevTime
        prevTime = currentTime
        count += 1
        if count == 100:
            print(elapsedTime/1000000000)
            elapsedTime = 0
            count = 0
        Update()
        if stop():
            break
        
        t.sleep(0.01)

        


def main():
    stop = False
    timer = threading.Thread(target=mainThread,args = (lambda: stop,))
    timer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop = True
        timer.join()    


if __name__ == "__main__":
    main()
    
