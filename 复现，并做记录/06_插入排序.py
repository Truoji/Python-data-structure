# 开发时间 2023/1/18 11:02

def insert_sort(alist):
    """插入排序"""
    n = len(alist)

    for j in range(n-1, 0, -1):   # 操作左边序列
        for i in range(1, n):   # 操作右边序列
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    insert_sort(li)
    print(li)