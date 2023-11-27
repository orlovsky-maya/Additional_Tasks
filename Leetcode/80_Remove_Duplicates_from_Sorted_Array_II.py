class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range((len(nums) - 1), 0, -1):
            if nums.count(nums[i]) > 2:
                del nums[i]

        k = len(nums)
        return k


num_s = [1, 1, 1, 2, 2, 3]
solution = Solution()
print(solution.removeDuplicates(num_s))

num_s = [0, 0, 1, 1, 1, 1, 2, 3, 3]

solution = Solution()
print(solution.removeDuplicates(num_s))

num_s = [1, 1, 1, 1]
solution = Solution()
print(solution.removeDuplicates(num_s))
