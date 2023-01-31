# 开发时间 2023/1/17 16:42

def Bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            # 代表从头走到尾
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    Bubble_sort(li)
    print(li)