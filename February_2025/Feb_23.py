class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n  # Initialize result with -1's.
        stack = []  # Stack to store indices
        
        for i in range(n):
            # While there's an index on the stack and current element is greater than that element
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]
            stack.append(i)
        
        return result

# Example usage:
# For input: 6 8 0 1 3
arr = [6, 8, 0, 1, 3]
sol = Solution()
res = sol.nextLargerElement(arr)
print(" ".join(map(str, res)))  # Expected Output: 8 -1 1 3 -1
