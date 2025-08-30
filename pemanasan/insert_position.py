class Solution(object):
    def searchInsert(self, nums, target):
        result =  0
        for i in range(len(nums)):
            if nums[i] == target:
                result = i
            elif nums[i] < target:
                result = i + 1

        return result
    
if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    solution = Solution()
    insert_position = solution.searchInsert(nums, target)
    print(insert_position)  