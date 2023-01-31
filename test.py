# 开发时间 2023/1/19 21:17
from typing import List

#
# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#
#     nums1 = nums1[0: m]
#     for i in range(n):
#         nums1.append(nums2[i])
#         i += 1
#     nums1.sort()
#
#
# if __name__ == '__main__':
#     print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        map