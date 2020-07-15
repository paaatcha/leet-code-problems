class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def backspaceList(L):
            new_l = list()
            for i,l in enumerate(L):                
                if l != "#":                
                    new_l.append(l)
                else:                    
                    if len(new_l) > 0:
                        new_l.pop(-1)

            return new_l

        new_s = backspaceList(S)
        new_t = backspaceList(T)

        return new_s == new_t
        


if __name__ == "__main__":
    sol = Solution()
    # ans = sol.backspaceCompare("ab#c", "ad#c")    
    # ans = sol.backspaceCompare("ab##", "c#d#")   
    # ans = sol.backspaceCompare("a##c", "#a#c")   
    ans = sol.backspaceCompare("a#c", "b")   
    print (ans)
