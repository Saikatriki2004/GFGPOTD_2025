class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        dictionary_set = set(dictionary)
        
        for i in range(1, n + 1):
            for word in dictionary_set:
                w_len = len(word)
                if i >= w_len and dp[i - w_len] and s.startswith(word, i - w_len, i):
                    dp[i] = True
                    break
        
        return dp[n]
