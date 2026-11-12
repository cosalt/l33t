class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums, count = set(nums), 1
        while count in nums:
            count += 1
        return count
