class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        local = 0
        ans = nums[0]
        for num in nums:
            local = max(num, local + num)
            ans = max(ans, local)
        return ans


if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print (ans)

    