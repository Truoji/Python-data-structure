# 开发时间 2023/1/17 9:33

class Node:
    """
    创建链表节点
    """

    def __init__(self, elem):
        self.elem = elem  # 给节点传入数据
        self.next = None  # 指向的下一个节点的地址


class SingleList():
    """
    实现一个单链表
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
        node.next = self.__head
        self.__head = node

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
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除指定元素"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    break
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next

    def seach(self, item):
        """查找某个元素"""
        cur = self.__head
        while cur is not None:
            if cur.elem ==item:
                print("找到了")
                return True
            else:
                print("不存在元素")
                cur = cur.next
        return False


if __name__ == '__main__':
    node1 = Node(111)
    ll = SingleList()
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

