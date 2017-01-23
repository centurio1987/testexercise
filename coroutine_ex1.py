import asyncio
import random
import time

@asyncio.coroutine
def producer():
    shared_list = []
    for i in range(20) :
        if not shared_list:
            shared_list.append(random.randrange(0,20))
        shared_list = yield from consumer(shared_list)
        print(shared_list)
        time.sleep(1)

@asyncio.coroutine
def consumer(shared_list):
    counter = 0
    counter += 1;
    if shared_list:
        print("consumer", shared_list.pop())
    return shared_list

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(producer())
    e = example()
    print(e)
