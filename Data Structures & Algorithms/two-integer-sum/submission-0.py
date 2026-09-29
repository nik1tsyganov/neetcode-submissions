class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            if nums[i] in n:
                return [n[nums[i]], i]
            else:
                n[target - nums[i]] = i