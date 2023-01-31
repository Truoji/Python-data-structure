# 开发时间 2023/1/18 10:40


def Bubble(alist):
    """冒泡法实现"""
    n = len(alist)   # 先获取长度

    for j in range(0, n):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    Bubble(li)
    print(li)