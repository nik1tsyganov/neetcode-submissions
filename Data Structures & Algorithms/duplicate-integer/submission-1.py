class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        res = {num: res.get(num, 0) + 1 for num in nums}
        return len(res) != len(nums)