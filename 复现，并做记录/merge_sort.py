# 开发时间 2023/1/19 16:25

def merge_sort(alist):
    n = len(alist)

    if n <= 1:
        return alist
    mid = n // 2

    # 将alist截成两段并且放入递归
    left_lst = merge_sort(alist[:mid])
    right_lst = merge_sort(alist[mid:])

    # 设置两个ptr
    left, right = 0, 0
    result = []

    while left < len(left_lst) and right < len(right_lst):
        if left_lst[left] < right_lst[right]:
            result.append(left_lst[left])
            left += 1

        else:
            result.append(right_lst[right])
            right += 1

    # 循环结束后，合并剩下的最后一个数
    result += left_lst[left:]
    result += right_lst[right:]
    return result


if __name__ == '__main__':
    li = [12, 512, 13, 44, 1210, 10, 12, 99]
    print(li)
    merge_sort(li)
    print(li)
    print(merge_sort(li))
