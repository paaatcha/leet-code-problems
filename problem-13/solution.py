class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        changed = 0

        for i in range(len(nums)): 

            if nums[i]:
                changed += 1
            else:
                changed -= 1

            if changed == 0:
                print("trocou")
        

if __name__ == "__main__":
    sol = Solution()    
    # ans = sol.findMaxLength([1,0,0,1,1,1,0,0,0,1,0,0])
    # ans = sol.findMaxLength([0,1,0])
    # ans = sol.findMaxLength([0,1])
    ans = sol.findMaxLength([0,1,1,0,1,1,1,0])

    print(ans)        