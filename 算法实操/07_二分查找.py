# 开发时间 2023/1/18 22:45

def binary_seach(alist, itrm):
    """二分查找递归调用"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == itrm:
            return True
        elif itrm < alist[mid]:
            return binary_seach(alist[:mid], itrm)
        else:
            return binary_seach(alist[mid+1:], itrm)
    return False


def binary_search2(alist, item):
    """二分查找在本列表上运用"""
    first = 0
    last = len(alist)
    mid = (first+last) // 2
    while first < last:
        if alist[mid] == item:
            return mid
        elif item < alist[mid]:
            alist = alist[first:mid]
        else:
            alist = alist[mid+1:last]
        mid //= 2
        last = len(alist)
    return False


def binary_sort(nums, target):
    left = 0
    right = len(nums) - 1
    # 使用左闭右闭区间
    while left <= right:
        mid = (right - left) // 2 + left  # 防止数据溢出，int型左右相加会导致数据溢出
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    li = [-1,0,3,5,9,12]
    print(li)
    print(binary_sort(li, 9))
    print(binary_sort(li, 11111))
    print(li)