# 开发时间 2023/1/18 13:53

def quick_sort(alist, first, last):
    """快排算法"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    higt = last

    while low < higt:
        # higt 左移
        while low < higt and alist[higt] > mid_value:
            higt -= 1
        alist[low] = alist[higt]
        # low += 1
        while higt > low and alist[low] <= mid_value:
            low += 1
        alist[higt] = alist[low]
        # higt -= 1
    # 从循环退出时， low == higt
    alist[low] = mid_value

    # 对low左边的执行快速排序
    quick_sort(alist, first, low-1)
    # 对low右边的列表执行快速排序
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
