class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         n = {}
         for num in nums:
            if num not in n:
                n[num] = 1
            else:
                return True

         return False