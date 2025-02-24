class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n  # To store the span for each day.
        stack = []      # Stack to store indices
        
        for i in range(n):
            # While the current element is greater than or equal to the element at the index on top of the stack, pop it.
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            
            # If stack is empty, no previous higher price exists.
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]
            
            # Push current index onto stack.
            stack.append(i)
        
        return span

# Example usage:
if __name__ == "__main__":
    # Read input (e.g., "100 80 60 70 60 75 85")
    arr = list(map(int, input().split()))
    sol = Solution()
    result = sol.calculateSpan(arr)
    # Print the output space-separated.
    print(" ".join(map(str, result)))
