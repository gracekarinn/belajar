# Leetcode repeated DNA sequences

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        temp = {}
        for i in range(len(s) - 9):
            temp[s[i:i + 10]] = temp.get(s[i:i + 10], 0) + 1
        return [key for key, value in temp.items() if value > 1]
    

if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    sol = Solution()
    print(sol.findRepeatedDnaSequences(s))


# Notes
# None. Future improvements could include using a more efficient data structure.
