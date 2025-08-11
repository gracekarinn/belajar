# Leetcode sqrt

class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

if __name__ == "__main__":
    x = 10
    sol = Solution()
    print(sol.mySqrt(x))

# Notes
# None. Future improvements could include optimizing the search range.