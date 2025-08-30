class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k


if __name__ == "__main__":
    nums = [3,3]
    val = 3
    solution = Solution()
    new_length = solution.removeElement(nums, val)
    print(new_length)