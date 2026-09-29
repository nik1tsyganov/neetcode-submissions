class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        return len({num: res.get(num, 0) + 1 for num in nums}) != len(nums)