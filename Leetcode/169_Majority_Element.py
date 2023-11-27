class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        count = 0
        result_num = nums[0]
        for n in s:
            if nums.count(n) > count:
                count = nums.count(n)
                result_num = n
        return result_num


num = [3, 2, 3]
solution = Solution()
print(solution.majorityElement(num))

num = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(num))

num = [6, 5, 5]
solution = Solution()
print(solution.majorityElement(num))