from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passedNums = dict()
        for i in range(len(nums)):
            complement =  target - nums[i]
            if complement in passedNums:
                return [passedNums[complement], i]
            passedNums[nums[i]] = i
        
        '''first try
        result = []
        for i in range(len(nums)-1,-1, -1):
            if (nums[i] - target) < 0:
                result.append(i)
                break
        for i in range(len(nums)):
            if (nums[i] + nums[result[0]]) == target:
                result.append(i)
                return result'''


instance = Solution()
nums = [1, 4, 5, 0, 1, 2, 0]
target = 0
result = instance.twoSum(nums, target)
print(result)
