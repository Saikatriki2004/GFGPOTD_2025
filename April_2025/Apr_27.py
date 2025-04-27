class Solution:
    def multiplyStrings(self, s1, s2):
        # Helper function to remove leading zeros
        def remove_leading_zeros(s):
            i = 0
            while i < len(s) and s[i] == '0':
                i += 1
            return s[i:] if i < len(s) else "0"
        
        # Step 1: Determine the sign
        sign1 = -1 if s1[0] == '-' else 1
        sign2 = -1 if s2[0] == '-' else 1
        sign = sign1 * sign2  # 1 for positive, -1 for negative
        
        # Step 2: Get absolute values
        abs_s1 = s1[1:] if sign1 == -1 else s1
        abs_s2 = s2[1:] if sign2 == -1 else s2
        
        # Step 3: Remove leading zeros
        num1 = remove_leading_zeros(abs_s1)
        num2 = remove_leading_zeros(abs_s2)
        
        # Step 4: Check for zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Step 5: Multiply the numbers
        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # Result array to hold digits
        
        # Multiply each digit pair and accumulate
        for i in range(m):
            for j in range(n):
                # Convert characters to integers using their digit value
                digit1 = ord(num1[m-1-i]) - ord('0')
                digit2 = ord(num2[n-1-j]) - ord('0')
                product = digit1 * digit2
                result[i + j] += product
        
        # Handle carries
        carry = 0
        for k in range(m + n):
            temp = result[k] + carry
            result[k] = temp % 10
            carry = temp // 10
        
        # Step 6: Build the result string
        res_str = []
        for k in range(m + n - 1, -1, -1):
            if not res_str and result[k] == 0:
                continue  # Skip leading zeros
            res_str.append(chr(result[k] + ord('0')))  # Convert digit to character
        prod_str = ''.join(res_str)
        
        # Attach sign if negative
        return prod_str if sign == 1 else '-' + prod_str
