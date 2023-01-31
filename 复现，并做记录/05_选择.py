# 开发时间 2023/1/18 10:51

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        idx = j
        for i in range(j+1, n):
            if alist[idx] > alist[i]:
                idx = i
        alist[j], alist[idx] = alist[idx], alist[j]


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    select_sort(li)
    print(li)