class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = dict()
        for a in strs:
            b = "".join(sorted(a))
            if b not in ans:
                ans[b] = [a]
            else:
                ans[b].append(a)

        return ans.values()
            

        
if __name__ == "__main__":
    sol = Solution()
    ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print (ans)