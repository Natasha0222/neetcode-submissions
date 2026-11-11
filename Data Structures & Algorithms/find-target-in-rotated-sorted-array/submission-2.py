from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            
            # Check if left half is sorted
            if nums[low] <= nums[middle]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # Otherwise, right half must be sorted
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
                    
        return -1