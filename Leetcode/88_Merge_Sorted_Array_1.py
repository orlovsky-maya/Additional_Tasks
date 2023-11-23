class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = n + m
        l1 = nums1.copy()[:m]
        l2 = nums2.copy()
        i_l1 = 0
        i_l2 = 0

        for i in range(length):
            if i_l1 == len(l1):
                nums1[i] = l2[i_l2]
                i_l2 += 1
            elif i_l2 == len(l2):
                nums1[i] = l1[i_l1]
                i_l1 += 1
            else:
                if l1[i_l1] < l2[i_l2]:
                    nums1[i] = l1[i_l1]
                    i_l1 += 1
                else:
                    nums1[i] = l2[i_l2]
                    i_l2 += 1
        print(nums1)


nums3 = [1, 2, 3, 0, 0, 0]
m1 = 3
nums4 = [2, 5, 6]
n1 = 3

solution = Solution()
solution.merge(nums3, m1, nums4, n1)

nums1 = [1]
m = 1
nums2 = []
n = 0

solution = Solution()
solution.merge(nums1, m, nums2, n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

solution = Solution()
solution.merge(nums1, m, nums2, n)

nums1 = [0]
m = 0
nums2 = [0]
n = 0

solution = Solution()
solution.merge(nums1, m, nums2, n)
