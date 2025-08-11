# Leetcode split the array 

class Solution(object):
    def isPossibleToSplit(self, nums):
        nums_dict = {}
        for i in set(nums):
            nums_dict[i] = nums.count(i)
            print(nums_dict)
        for key, value in nums_dict.items():    
            if value > 2:
                return False
        return True

if __name__ == "__main__":
    list = [1,1,1,1]
    sol = Solution()
    print(sol.isPossibleToSplit(list))

# Notes:
# .items() iterate through the items
# set() creates a set object that iterate through the unique elements of the list
