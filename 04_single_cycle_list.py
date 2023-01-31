# 开发时间 2023/1/17 13:53
# 开发时间 2023/1/17 9:33

class Node:
    """
    创建链表节点
    """

    def __init__(self, elem):
        self.elem = elem  # 给节点传入数据
        self.next = None  # 指向的下一个节点的地址


class SingleCycleList():
    """
    实现一个单向循环链表
    """

    def __init__(self, node=None):
        """实现初始化链表头，如果传入数据，初始化一个地址"""
        self.__head = node
        if node:
            node.next = node    # 设置回环

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def lenth(self):
        """返回链表长度"""
        cur = self.__head  # cur 记录当前链表头的信息
        if self.is_empty():
            return 0
        count = 1  # count计数，用来统计整个链表长度
        while cur.next is not self.__head:
            count += 1
            cur = cur.next  # 移动地址，利用next来寻找
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环的时候，cur指向尾节点，没有进循环未打印
        print(cur.elem)

    def add(self, item):
        """在链表头添加元素， 头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环的时候，cur指向尾节点
            node.next = self.__head
            self.__head = node
            # cur.next = node  两种写法都可以
            cur.next = self.__head

    def append(self, item):
        """在链表尾部插入，尾插法"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环的时候，cur指向尾节点
            # cur.next = node
            # node.next = self.__head
            # 或者
            node.next = cur.next    # node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置插入元素"""
        node = Node(item)
        pre = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > self.lenth():
            self.append(item)
        else:
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除指定元素"""
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur.next is not self.__head:
            if cur.elem == item:
                # 检查是否是头结点
                # 头节点
                if cur == self.__head:
                    # 先找到尾节点
                    # 创建新的游标
                    rear = self.__head
                    while rear is not self.__head:
                        rear = rear.next
                    # 退出循环后  rear  指向尾节点
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环后 cur指向尾节点，单独判断
        if cur.elem == item:
            if cur == self.__head:   # 链表只有一个节点
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head

    def seach(self, item):
        """查找某个元素"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环后， cur指向尾结点，再进行一次判断
        if cur.elem == item:
            return True
        else:
            return False


if __name__ == '__main__':
    ll = SingleCycleList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.travel()
    ll.append(0)
    ll.travel()
    ll.insert(2, 90)
    ll.travel()
    ll.add(2)
    ll.travel()
    ll.remove(2)
    ll.travel()
