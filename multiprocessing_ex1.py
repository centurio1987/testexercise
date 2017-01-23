from multiprocessing import Process, Queue, Event

def add(a, b):
    return a+b

if __name__ == '__main__':
    proc1 = Process(target=add, args=(1, 2))
    proc2 = Process(target=add, args=(2,3))
    proc3 = Process(target=add, args=(3,4))
    proc_list = []

    proc_list.append(proc1.start())
    proc_list.append(proc2.start())
    proc_list.append(proc3.start())

    proc1.join()
    proc2.join()
    proc3.join()
