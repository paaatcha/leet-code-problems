class MinStack(object):     

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = list()        
        self.global_min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.global_min is None:
            self.global_min = x            
        elif x < self.global_min:            
            self.global_min = x            
            
        node = (x, self.global_min)        
        self.values.insert(0, node)    
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.values) != 0:
            self.values.pop(0)
            if len(self.values) == 0:
                self.global_min = None
            else:
                self.global_min = self.values[0][1]
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.values) == 0:
            return None
        else:        
            return self.values[0][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.values) == 0:
            return None
        else:        
            return self.values[0][1]
        


if __name__ == "__main__":
    stack = MinStack()    
    stack.push(-10)
    stack.push(14)
    print(stack.getMin())
    print(stack.getMin())
    stack.push(-20)
    print(stack.getMin())
    print(stack.getMin())
    print(stack.top())
    print(stack.getMin())
    stack.pop()
    stack.push(10)
    stack.push(-7)
    print(stack.getMin())
    stack.push(-7)
    stack.pop()
    print(stack.top())
    print(stack.getMin())
    stack.pop()
