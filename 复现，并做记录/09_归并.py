# 开发时间 2023/1/18 22:04

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    # 分成只剩下一个元素时停止
    if n <= 1:
        return alist
    mid = n // 2

    # 分成两半，并使用递归，使他们继续分
    left_lst = merge_sort(alist[:mid])
    right_lst = merge_sort(alist[mid:])

    # 合并
    left_ptr, right_ptr = 0, 0
    result = []

    while left_ptr < len(left_lst) and right_ptr < len(right_lst):
        if left_lst[left_ptr] <= right_lst[right_ptr]:
            result.append(left_lst[left_ptr])
            left_ptr += 1
        else:
            result.append(right_lst[right_ptr])
            right_ptr += 1

    # 循环结束后，合并两个列表
    result += left_lst[left_ptr:]
    result += right_lst[right_ptr:]
    return result


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12, 99]
    print(li)
    merge_sort(li)
    print(li)
    print(merge_sort(li))