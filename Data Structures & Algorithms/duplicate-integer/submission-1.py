class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for i ,num in enumerate(nums):
            if num in numbers:
                return True
            numbers[num]=i
        return False

        