# 开发时间 2023/1/18 9:57
# 开发时间 2023/1/17 22:42


"""实现一个循环单链表类"""


class Node:
    """节点"""

    def __init__(self, elem):
        self.elem = elem  # 实现初始化数据
        self.next = None  # 初始化结点，类似指针的操作


class SingleCycleListLink:
    """单链表"""

    def __init__(self, node=None):
        """初始画链表头"""
        self.__head = node

    def is_empty(self):
        """判断链表是否为空
        判断链表头的结点是否为 None 为真则返回
        """
        return self.__head is None

    def lenth(self):
        """计算链表长度"""
        cur = self.__head  # 定义当前游标位置
        # 从头遍历     考虑特殊情况：空链表的时候，cur == None，不进入循环，直接返回count
        if self.is_empty():
            return 0
        else:
            count = 1  # 计数
            while cur.next is not self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        # 考虑特殊情况，空链表时：cur == None 不进入循环
        if self.is_empty():
            return
        while cur.next is not self.__head:
            print(cur.elem, end=" ")    # 要先打印当前的元素，再移动 cur
            cur = cur.next
        # 退出循环的时候，cur指向尾节点
        print(cur.elem)

    def add(self, item):
        """在表链表头插入元素 item"""
        node = Node(item)      # 初始化一个结点
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:      # 遍历拿到尾节点
                cur = cur.next
            node.next = self.__head     # 先将node的下一个指向链接链表头，防止将链表打乱
            self.__head = node      # 最后把结点和链表头连接上
            cur.next = node

    def append(self, item):
        """再链表尾部添加元素 item ，尾插法"""
        node = Node(item)
        cur = self.__head
        # 考虑特殊情况：空链表：cur.next不存在
        if self.is_empty():
            self.__head = node  # 直接将 self.__head 指向 node
            node.next = node
        else:
            while cur.next is not self.__head:     # 使用 cur.next 防止 cur 移动到None
                cur = cur.next
            # 退出循环后 连接链表头
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """在指定位置插入元素 item"""
        # 需要两个游标来定位
        pre = self.__head
        node = Node(item)
        # 考虑特殊情况：pos小于0   在这不实现反向插入  直接调用 add()
        if pos <= 0:
            self.add(item)
        # 考虑特殊情况，超过了链表长度，选择直接在结尾添加元素
        elif pos > self.lenth():
            self.append(item)
        else:
            count = 0   # 用来和pos做判断，定位位置
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 定位到位置以后插入结点 pre指向pos-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除链表中的元素"""
        cur = self.__head
        pre = None
        # 考虑特殊情况：空链表
        if self.is_empty():
            return
        else:
            while cur.next is not self.__head:
                if cur.elem == item:
                    # 考虑特殊情况：判断该节点是否是头节点
                    if cur == self.__head:
                        # 尾节点
                        rear = self.__head
                        while rear.next is not self.__head:
                            rear= rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    else:
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
        # 退出循环后 cur指向尾节点，单独判断
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            pre.next = self.__head

    def seach(self, item):
        """查找链表元素是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    node2 = Node(100)
    ll = SingleCycleListLink()
    # print(ll.is_empty())
    # print(ll.lenth())
    ll.travel()
    ll.add(3)
    ll.add(2)
    ll.travel()
    ll.append(4)
    ll.travel()
    ll.insert(0, 1)
    ll.travel()
    ll.insert(10, 5)
    ll.travel()
    ll.insert(2, 100)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(1)
    ll.travel()
    ll.remove(5)
    ll.travel()
