'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    1) Open brackets must be closed by the same type of brackets.
    2) Open brackets must be closed in the correct order.
    3) Every close bracket has a corresponding open bracket of the same type.
'''

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

def main():
    #example input
    string = '(({[]}))'
    instance = Solution()
    result = instance.isValid(string)
    print(result)

if __name__ == '__main__':
    main()
