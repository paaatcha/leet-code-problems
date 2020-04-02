class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            x ^= num
            
        return x

if __name__ == "__main__":
    sol = Solution()
    ans = sol.singleNumber([1,2,2,3,3])
    print (ans)

    