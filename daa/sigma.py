class Solution(object):
    def sigma(self, total, nums):
        nums = nums.split(" ")
        add = 0
        for i in range(total):
            add += int(nums[i])
        return add

if __name__ == "__main__":
    N = int(input())
    sigma_input = input()
    sol = Solution()
    print(sol.sigma(N, sigma_input))
