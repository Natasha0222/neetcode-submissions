from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        position=bisect_left(nums,target)
        if position<len(nums) and nums[position]==target:
            return position
        return -1


        