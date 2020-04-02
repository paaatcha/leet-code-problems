class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_powers = sum([int(c_num)**2 for c_num in str(n)])
        if n < 10:
            if n == 1 or n == 7:
                return 1
            else:
                return 0
        else: 
            return self.isHappy(sum_powers)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.isHappy(368)
    print (ans)

    