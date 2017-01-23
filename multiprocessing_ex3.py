import concurrent.futures
import time

def producer(shared_list, cnt):
    shared_list.append(cnt)
    return shared_list

def consumer(future):
    print("consumer", future.result().pop())

if __name__ == "__main__":
    shared_list = []
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        future = [executor.submit(producer, shared_list, i) for i in range(20)]
        #executor.submit(consumer(future))

        for future in concurrent.futures.as_completed(future):
            pass

        time.sleep(2)
        print(shared_list)
