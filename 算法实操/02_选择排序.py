# 开发时间 2023/1/17 20:03

def Select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):  # j:0 ~ n-2
        min_idx = j
        for i in range(1+j, n):
            if alist[min_idx] > alist[i]:
                min_idx = i
        alist[j], alist[min_idx] = alist[min_idx], alist[j]


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    Select_sort(li)
    print(li)
