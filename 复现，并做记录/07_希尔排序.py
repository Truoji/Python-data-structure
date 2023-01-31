# 开发时间 2023/1/18 17:18

def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2

    while gap > 0:
        # 实现从步长gap往后计算
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                i -= gap
        gap //= 2


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    shell_sort(li)
    print(li)
