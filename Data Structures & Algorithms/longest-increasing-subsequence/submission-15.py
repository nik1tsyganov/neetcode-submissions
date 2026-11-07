class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp = [1] * n

        for i in range(1, n):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
        
        return max(dp)