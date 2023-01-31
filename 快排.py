# 开发时间 2023/1/24 19:31


def quick_sort(alist, first, last):
    """快排算法"""
    if first >= last:
        return

    mid_val = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] > mid_val:
            high -= 1
        alist[low] = alist[high]

        while high > low and alist[low] <= mid_val:
            low += 1
        alist[high] = alist[low]

    alist[high] = mid_val

    quick_sort(alist, first, low - 1)
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12, 99]
    print(li)
    quick_sort(li,0, len(li)-1)
    print(li)
