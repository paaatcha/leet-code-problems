class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)     
        pas = 1
        k = 1
        while(k<=pas):
            pas = 0            
            for i in range(size-1):            
                if nums[i] == 0:
                    nums[i] = nums[i+1]
                    nums[i+1] = 0
                    pas+=1
            k+=1

        return nums        

if __name__ == "__main__":
    sol = Solution()
    ans = sol.moveZeroes([0,1,0,3,12])
    print (ans)