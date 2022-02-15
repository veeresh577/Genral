from threading import Thread
import time


def timer(name, delay, repeat):
    print("timer" + name + "started")
    while repeat > 0:
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))
        repeat -= 1
    print("timer" + name + "compleated")


def main():
    t1 = Thread(target=timer, args=("timer1", 2, 5))
    t2 = Thread(target=timer, args=("timer2", 4, 5))
    t1.start()
    t2.start()
    p = int(input("enter a number\n"))
    time.sleep(1)
    print(p+1)


if __name__ == '__main__':
    main()
