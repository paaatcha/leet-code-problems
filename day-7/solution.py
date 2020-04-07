class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        elements = {x: False for x in range(1002)}
        for a in arr:
            elements[a] = True

        for a in arr:
            if elements[a+1]:
                ans+=1

        return ans


if __name__ == "__main__":
    sol = Solution()
    # ans = sol.countElements([1,2,3])
    # ans = sol.countElements([1,1,3,3,5,5,7,7])
    # ans = sol.countElements([1,3,2,3,5,0])
    ans = sol.countElements([1,1,2,2])    
    print (ans)
