class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)):
            if i < m:
                nums1[i] = nums1[i]
            else:
                nums1[i] = nums2[i - m]
        nums1.sort()
        cnt = m + n
        result = nums1[:cnt]
        return result 

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution = Solution()
    merged_array = solution.merge(nums1, m, nums2, n)