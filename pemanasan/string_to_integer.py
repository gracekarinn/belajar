# Leetcode string to integer(atoi)

class Solution(object):
    def myAtoi(self, s):
        a = s.lstrip()
        a = list(a)
        MIN = -2**31
        MAX = 2**31 - 1
        print(a)
        temp = ""
        for i in range(len(a)):
           if a[i].isdigit() or (i == 0 and a[i] in ['-', '+']):
                temp += a[i]
           else:
               break
        if temp.startswith('+') and len(temp) > 1:
            num = int(temp)
        elif temp.startswith('-') and len(temp) > 1:
            num = -int(temp[1:])
        elif temp.isdigit():
            num = int(temp)
        else:
            num = 0

        if num < MIN:
            return MIN
        if num > MAX:
            return MAX
        return num


if __name__ == "__main__":
    s = ""
    sol = Solution()
    print(sol.myAtoi(s))


# Notes:
# Used string so I can easily handle the symbol.
# The logic can be further improved... as long as it works I guess
