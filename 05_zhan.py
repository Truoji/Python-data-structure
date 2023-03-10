# 开发时间 2023/1/17 15:29
class Stack:
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新元素到栈顶"""
        # self.__list.append(item)
        return self.__list.insert(0, item)

    def pop(self):
        """弹出栈顶元素"""
        # return self.__list.pop()
        return self.__list.pop(0)

    def peek(self):
        """返回栈顶元素"""
        # 如果列表不为空
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(6)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())