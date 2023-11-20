class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums) - 1, 0, -1):
            if nums.count(nums[i]) > 1:
                del nums[i]
        print(nums)
        k = len(nums)
        return k


nums = [1, 1, 2]
solution = Solution()
print(solution.removeDuplicates(nums))

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3 , 4]

solution = Solution()
print(solution.removeDuplicates(nums))

nums = [1, 1, 1, 1]
solution = Solution()
print(solution.removeDuplicates(nums))
