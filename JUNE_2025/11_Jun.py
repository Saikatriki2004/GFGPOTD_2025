class Solution:
    def findLength(self, color, radius):
        stack = []
        for c, r in zip(color, radius):
            # compare tuples directly
            if stack and stack[-1] == (c, r):
                stack.pop()
            else:
                stack.append((c, r))
        return len(stack)

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([2, 3, 5], [3, 3, 5]))  # prints 3
