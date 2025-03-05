class Solution:
    def longestStringChain(self, words):
        # Dictionary to store the longest chain length ending at each word
        dp = {}
        max_chain = 0
        
        # Process words in order of increasing length
        for w in sorted(words, key=len):
            # Initialize chain length for current word
            dp[w] = 1
            
            # Check all possible predecessors by removing one character
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]  # Remove character at index i
                if pred in dp:  # If predecessor has been processed
                    dp[w] = max(dp[w], dp[pred] + 1)
            
            # Update the maximum chain length
            max_chain = max(max_chain, dp[w])
        
        return max_chain
