# 开发时间 2023/1/17 20:53

def Insert_sort(alist):
    """插入算法"""

    n = len(alist)
    # 从右边的无需序列中取出多少个元素执行循环
    for j in range(1, n):
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素， 即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i = i - 1
            else:
                break


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    Insert_sort(li)
    print(li)