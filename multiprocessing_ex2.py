from multiprocessing import Queue, Process
import time

def produce(q):
    for i in range(20):
        q.put(i)
        time.sleep(2)

def consume(q):
    while(1):
        if q.empty() == False:
            continue
        else:
            print(q.get())

if __name__ == "__main__":
    queue = Queue(3)
    producer = Process(target=produce, args=(queue,))
    consumer = Process(target=consume, args=(queue,))
    Process()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
