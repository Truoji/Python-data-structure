# 开发时间 2023/1/17 10:54

from danlianbiao import SingleList

class Node:
    """双链表节点 """
    def __init__(self, item):
        """
        实现双向链表
        :param elem: 节点元素
        """
        self.elem = item
        self.next = None    # 后继节点
        self.prev = None    # 前驱节点   或者叫prior


class DoubleLinkList():
    """定义链表
        使用继承，继承来自单链表的成员方法
    """

    def __init__(self, node=None):
        """实现初始化链表头，如果传入数据，初始化一个地址"""
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def lenth(self):
        """返回链表长度"""
        cur = self.__head   # cur 记录当前链表头的信息
        count = 0   # count计数，用来统计整个链表长度
        while cur is not None:
            count += 1
            cur = cur.next  # 移动地址，利用next来寻找
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        """在链表头添加元素， 头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node

    def append(self, item):
        """在链表尾部插入，尾插法"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置插入元素"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.lenth():
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除指定元素"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 判断是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                    break
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


    def seach(self, item):
        """查找某个元素"""
        cur = self.__head
        while cur is not None:
            if cur.elem ==item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    node1 = Node(111)
    ll = DoubleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(4)
    print(ll.lenth())
    ll.travel()
    ll.insert(0, 9)
    ll.insert(3, 12)
    ll.travel()
    ll.remove(2)
    ll.travel()
    ll.seach(9)