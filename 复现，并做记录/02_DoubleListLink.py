# 开发时间 2023/1/17 23:55
# 开发时间 2023/1/17 22:42


"""实现一个双向链表链表类"""

class Node:
    """节点"""

    def __init__(self, elem):
        self.elem = elem  # 实现初始化数据
        self.next = None  # 初始化结点，类似指针的操作    后继结点
        self.prev = None  # 初始化前驱结点


class DoubleLinkLiset:
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
        count = 0  # 计数
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        # 考虑特殊情况，空链表时：cur == None 不进入循环
        while cur is not None:
            print(cur.elem, end=" ")    # 要先打印当前的元素，再移动 cur
            cur = cur.next
        print("")   # 打印换行

    def add(self, item):
        """在表链表头插入元素 item"""
        node = Node(item)  # 初始化一个结点
        # 考虑特殊情况：空链表
        if self.is_empty():
            self.__head = node
            return
        else:
            # 将node的下一个指向链接链表头，防止将链表打乱
            node.next = self.__head
            self.__head = node  # 然后把结点和链表头连接上
            node.next.prev = node   # 最后把node下一个结点的前驱结点指向回node

    def append(self, item):
        """再链表尾部添加元素 item ，尾插法"""
        node = Node(item)
        cur = self.__head
        # 考虑特殊情况：空链表：cur.next不存在
        if self.is_empty():
            self.__head = node  # 直接将 self.__head 指向 node
        else:
            while cur.next is not None:  # 使用 cur.next 防止 cur 移动到None
                cur = cur.next
            # 退出循环后 连接链表头
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置插入元素 item"""
        # 需要两个游标来定位
        cur = self.__head
        node = Node(item)
        # 考虑特殊情况：pos小于0   在这不实现反向插入  直接调用 add()
        if pos <= 0:
            self.add(item)
        # 考虑特殊情况，超过了链表长度，选择直接在结尾添加元素
        elif pos > self.lenth():
            self.append(item)
        else:
            count = 0  # 用来和pos做判断，定位位置
            while count < pos:
                count += 1
                cur = cur.next
            # 定位到位置以后插入结点 pre指向pos-1位置
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除链表中的元素"""
        cur = self.__head
        # 考虑特殊情况：空链表
        if self.is_empty():
            return
        else:
            while cur is not None:
                if cur.elem == item:
                    # 考虑特殊情况：判断该节点是否是头节点
                    if cur == self.__head:
                        # 头节点，但是不一定是单链表
                        self.__head = cur.next
                        if cur.next is not None:
                            # 判断链表是否只有一个结点
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
        """查找链表元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    node2 = Node(100)
    ll = DoubleLinkLiset()
    ll.travel()
    ll.add(3)
    ll.add(2)
    ll.add(1)
    ll.travel()
    ll.append(90)
    # print(ll.is_empty())
    ll.travel()
    ll.insert(0, 0)
    ll.insert(3, 10)
    ll.insert(9, 120)
    ll.travel()
    ll.remove(0)
    ll.travel()
