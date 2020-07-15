class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
                 
        
        while len(stones) > 1:
            stones.sort()
            m1 = stones.pop()
            m2 = stones.pop()
            if m1 != m2:
                stones.append(m1-m2)

        return 0 if len(stones) == 0 else stones[0]
        

if __name__ == "__main__":
    sol = Solution()
    # ans = sol.lastStoneWeight([2,7,4,1,8,1])
    ans = sol.lastStoneWeight([2,2])

    print(ans)
        