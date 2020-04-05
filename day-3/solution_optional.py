class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size = len(nums)
        max_sum = min(nums)

        for i in range(size):            
            local_sum = 0
            for j in range(i, size):                
                local_sum += nums[j]
                max_sum = max(local_sum, max_sum)

        return max_sum       

if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print (ans)

    