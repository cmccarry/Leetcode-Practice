'''
Given an integer array nums, return:
    True if any value appears at least twice in the array
    False if every element is distinct.
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False

def main():
    #example input
    nums = [0, 1, 2, 3, 1]
    instance = Solution()
    result = instance.containsDuplicate(nums)
    print(result)

if __name__ == '__main__':
    main()
    