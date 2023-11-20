class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort(key=lambda n: n == val)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]

        k = len(nums)
        return k


nums = [3, 2, 2, 3]
val = 3

solution = Solution()
print(solution.removeElement(nums, val))


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

solution_2 = Solution()
print(solution_2.removeElement(nums, val))

nums = [1]
val = 1

solution_2 = Solution()
print(solution_2.removeElement(nums, val))

