# Problem 10: Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example 1:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```
**hint**: Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

# About the solution
Well, it's just a stack implementation. The only part that is different from a standard stack is the minimun retrieval. However, they gave us the solution in the hint. 

Just an observation, I implemented the stack using the method `insert`. It's also possible to implement using the `append`. In this case, the methods `top()` and `pop()` must act in the last element of `values`, that is, `values[-1]`.