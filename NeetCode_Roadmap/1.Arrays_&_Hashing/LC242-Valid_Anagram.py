class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = dict()

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char in t:
            frequency[char] = frequency.get(char, 0) - 1
        
        for value in frequency.values():
            if value != 0:
                return False
        
        return True

#example input
input1 = ('thing')
input2 = ('night')
instance = Solution()
result = instance.isAnagram(input1,input2)
print(result)
