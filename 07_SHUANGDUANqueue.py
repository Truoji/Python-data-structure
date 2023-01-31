# 开发时间 2023/1/17 16:21

class Dequeue:
    """双端队列"""

    def __init__(self):
        self.__queue = []

    def add_front(self, item):
        """在队列中添加一个元素"""
        self.__queue.insert(0, item)

    def add_end(self, item):
        """在队列中添加一个元素"""
        self.__queue.append(item)

    def pop_front(self):
        """在队列头部删除一个元素"""
        return self.__queue.pop(0)

    def pop_end(self):
        """在队列头部删除一个元素"""
        return self.__queue.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__queue == []

    def size(self):
        """判断队列长度"""
        return len(self.__queue)


if __name__ == '__main__':
    q = Dequeue()
    q.add_front(1)
    q.add_front(2)
    q.add_end(3)
    q.add_end(4)

    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_end())
    print(q.pop_end())