# 开发时间 2023/1/19 16:00

def quick_sort(alist, first, last):
    """快速排序"""

    if first >= last:
        return
    mid_val = alist[first]
    left = first
    right = last

    while left < right:
        while left < right and alist[right] > mid_val:
            right -= 1
        alist[left] = alist[right]

        while right > left and alist[left] <= mid_val:
            left += 1
        alist[right] = alist[left]

    alist[left] = mid_val
    # 循环结束后，将 mid_val放到中间位置，用low或者high都可以
    quick_sort(alist, first, left - 1)
    quick_sort(alist, left + 1, last)


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12, 99]
    print(li)
    quick_sort(li,0, len(li)-1)
    print(li)

