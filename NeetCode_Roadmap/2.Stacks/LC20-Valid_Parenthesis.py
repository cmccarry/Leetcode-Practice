class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        for character in string:
            if character in "({[":
                stack.append(character)
            else:
                #if stack is empty or closing bracket doesn't match last opening bracket in stack
                if not stack or \
                    (character == ")" and stack[-1] != '(') or \
                    (character == "}" and stack[-1] != '{') or \
                    (character == "]" and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack    # == not bool(stack), returns true if empty

#example input
string = '(({[]}))'
instance = Solution()
result = instance.isValid(string)
print(result)