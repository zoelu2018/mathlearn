from Queue import Queue
def hotPotato(namelist,num):
    simqueue = Queue() #空队列
    for name in namelist:
        simqueue.enqueue(name) # 添加在队尾
    while simqueue.size>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) #移除队列的头部
        simqueue.dequeue()
    return simqueue.dequeue()