import bisect

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    _sieve = None
    _primes = None

    def __init__(self):
        if Solution._sieve is None:
            max_limit = 10**5
            sieve = [False, False] + [True] * (max_limit - 1)
            for i in range(2, int(max_limit ** 0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, max_limit + 1, i):
                        sieve[j] = False
            Solution._sieve = sieve
            Solution._primes = [i for i, is_p in enumerate(sieve) if is_p]
        
    def primeList(self, head):
        current = head
        sieve = Solution._sieve
        primes = Solution._primes
        while current:
            val = current.val
            if not sieve[val]:
                idx = bisect.bisect_left(primes, val)
                left = primes[idx - 1] if idx > 0 else None
                right = primes[idx] if idx < len(primes) else None
                candidates = []
                if left is not None:
                    candidates.append(left)
                if right is not None:
                    candidates.append(right)
                if candidates:
                    min_dist = float('inf')
                    nearest = None
                    for p in candidates:
                        d = abs(val - p)
                        if d < min_dist:
                            min_dist = d
                            nearest = p
                        elif d == min_dist:
                            nearest = min(nearest, p) if nearest is not None else p
                    current.val = nearest
            current = current.next
        return head
