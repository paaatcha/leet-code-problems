class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        pos = 0
        for i in range(size):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos+=1

        for i in range(pos, size):
            nums[i] = 0

        return nums
        

if __name__ == "__main__":
    sol = Solution()
    ans = sol.moveZeroes([0,1,0,3,12])
    print (ans)