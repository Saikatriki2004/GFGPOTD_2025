class Solution:
    def __init__(self):
        # Initialize two stacks
        self.main_stack = []  # Stores all elements
        self.min_stack = []   # Tracks minimum elements

    def push(self, x):
        # Add element to main stack
        self.main_stack.append(x)
        # Add to min_stack if it's empty or x is less than or equal to current min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # Only pop if main_stack is not empty
        if self.main_stack:
            popped = self.main_stack.pop()
            # If popped element is the current min, remove it from min_stack
            if self.min_stack and popped == self.min_stack[-1]:
                self.min_stack.pop()

    def peek(self):
        # Return top element or -1 if empty
        return self.main_stack[-1] if self.main_stack else -1

    def getMin(self):
        # Return current minimum or -1 if empty
        return self.min_stack[-1] if self.min_stack else -1
