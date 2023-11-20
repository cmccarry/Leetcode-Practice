'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()

        for word in strs:
            sorted_string = (sorted(word))
            print(sorted_string)

            if sorted_string not in my_dict:
                my_dict[sorted_string] = []

            my_dict[sorted_string].append(word)
            print(my_dict)

        return list(my_dict.values())
        
def main():
    instance = Solution()
    print(instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == '__main__':
    main()
