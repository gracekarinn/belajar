# Leetcode roman to int

class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500,
                 "M": 1000}
        
        result = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[-1]]
        return result

                
if __name__ == "__main__":
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))

# Note: lol i need to learn more about this
        