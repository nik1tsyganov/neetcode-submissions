import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(nums, low, high, rank): 
            nums[high], nums[rank] = nums[rank], nums[high]
            last = low - 1
            for i in range(low, high):
                if nums[high] >= nums[i]:
                    last += 1
                    nums[last], nums[i] = nums[i], nums[last]
            
            nums[last + 1], nums[high] = nums[high], nums[last + 1]
            return last + 1
        
        low, high, rank = 0, len(nums) - 1, len(nums) - k

        while True:
            if low == high:
                return nums[low]
            
            rand = random.randint(low, high)
            pivot = partition(nums, low, high, rand)
            target = pivot

            if target > rank:
                high = pivot - 1
            elif target == rank:
                return nums[pivot]
            else:
                low = pivot + 1