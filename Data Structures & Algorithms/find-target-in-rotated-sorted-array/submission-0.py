class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def split(nums, low, high, target):
            if low == high:
                return low if target == nums[low] else -1
            
            mid = (high + low) // 2
            left = split(nums, low, mid, target)
            right = split(nums, mid + 1, high, target)
            return left if left != -1 else right
        
        return split(nums, 0, len(nums) - 1, target)