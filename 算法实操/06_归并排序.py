# 开发时间 2023/1/18 15:25

def merge_sort(alist):
    """归并排序算法"""
    n = len(alist)

    # 实现拆分
    if n <= 1:
        return
    mid = n // 2
    # left采用归并排序后形成的新的列表
    left_lst = merge_sort(alist[:mid])
    # left采用归并排序后形成的新的列表
    right_lst = merge_sort(alist[mid:])

    # 将两个有序的子序列进行合并
    # merge(left, right)



