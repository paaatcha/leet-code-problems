class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        size = len(nums)
            
        prod = [1] * size

        for i in range(1, size):
            prod[i] = prod[i - 1] * nums[i - 1]


        print(prod)
            
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            prod[i] = prod[i] * right_product

        return prod
        

if __name__ == "__main__":
    sol = Solution()    
    ans = sol.productExceptSelf([2,2,3,4])

    print(ans)        