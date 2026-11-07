class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lim = n // 3
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        return [key for key, value in freq.items() if value > lim]