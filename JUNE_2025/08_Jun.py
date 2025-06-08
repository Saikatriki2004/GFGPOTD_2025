class Solution:
    def isSumString(self, s: str) -> bool:
        n = len(s)
        # Try every possible split point i,j for the first two numbers:
        # s[0:i], s[i:j], and the rest must follow
        for i in range(1, n - 1):
            # first number = s[0:i]
            # skip if it has leading zeroes (but allow "0")
            if s[0] == '0' and i > 1:
                break
            
            for j in range(i + 1, n):
                # second number = s[i:j]
                if s[i] == '0' and j - i > 1:
                    break
                
                # parse the first two
                num1 = int(s[0:i])
                num2 = int(s[i:j])
                
                # now try to consume the rest of the string
                k = j
                count = 2  # we've already got two numbers
                while k < n:
                    num3 = num1 + num2
                    sum_str = str(num3)
                    L = len(sum_str)
                    
                    # must match the next L chars
                    if k + L > n or s[k:k+L] != sum_str:
                        break
                    
                    # advance window
                    k += L
                    num1, num2 = num2, num3
                    count += 1
                    
                # if we reached exactly the end with ≥3 numbers, it's valid
                if k == n and count >= 3:
                    return True
        
        return False
