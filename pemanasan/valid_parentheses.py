# Leetcode valid parentheses

class Solution(object):
    def isValid(self, s):
        parentheses = ['(', ')', '{', '}', '[', ']']
        stack = []

        for i in s:
            if i not in parentheses or len(s) <= 1:
                return False
            if i in [")", "}", "]"] and len(stack) == 0:
                return False
            if i in ["(", "{", "["]:
                stack.append(i)
            elif i == ")" and stack.pop() == "(":
                continue
            elif i == "]" and stack.pop() == "[":
                continue
            elif i == "}" and stack.pop() == "{":
                continue
            else:
                return False

        result = False if stack else True
        
        return result
    
if __name__ == "__main__":
    s = "){"
    sol = Solution()
    print(sol.isValid(s))

# Note: It is not very efficient. Too many if-else statements can be simplified.