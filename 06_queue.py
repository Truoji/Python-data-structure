# 开发时间 2023/1/17 15:47

class Queue:
    """队列"""

    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        """在队列中添加一个元素"""
        self.__queue.append(item)

    def dequeue(self):
        """在队列头部删除一个元素"""
        return self.__queue.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__queue == []

    def size(self):
        """判断队列长度"""
        return len(self.__queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())