class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while True:
            if low == high:
                if nums[low] == target:
                    return low
                return -1
            
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid 