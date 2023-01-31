# 开发时间 2023/1/18 17:33

def quick_sort(alist, first, last):

    # 递归结束条件, 需要放在最开始，否则回导致下面的值赋值后打乱
    if first >= last:
        return
    low = first
    high = last
    mid_val = alist[first]

    # RecursionError: maximum recursion depth exceeded while calling a Python object
    # 如果使用 first == last 这个判断条件，会导致进入递归死循环
    # if first == last:
    #     return

    while low < high:
        # 当我的low坐标小于high坐标的时候，如果 alist[high] 比 中间的 mid_val 大
        # 那么将high的作为位置向左移动 1
        while low < high and alist[high] > mid_val:
            high -= 1
        # 当不满足循环条件的时候 即 low>=high或者alist[high]的值传给alist[low] 然后进入下一个判断
        alist[low] = alist[high]

        # 当我的high坐标还在low坐标的右边的时候，如果我的alist[low]比mid_val小
        # 那么我的当前位置不动，然后移动low坐标
        while high > low and alist[low] <= mid_val:
            low += 1
        # 当不满足循环条件：即high的坐标移动到中间位置或者  alist[low]大于mid_val，要把他往mid_val的右边移动
        alist[high] = alist[low]

    # 循环结束后，将 mid_val放到中间位置，用low或者high都可以
    alist[high] = mid_val

    # 进行递归快排
    quick_sort(alist, first, low-1)     # 实现mid_val的左半边排序
    quick_sort(alist,low+1, last)       # 实现右半边排序


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12, 99]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
