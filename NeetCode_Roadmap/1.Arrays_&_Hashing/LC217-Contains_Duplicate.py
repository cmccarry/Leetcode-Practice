from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False

nums = [0, 1, 2, 3, 1]
instance = Solution()
result = instance.containsDuplicate(nums)
print(result)
