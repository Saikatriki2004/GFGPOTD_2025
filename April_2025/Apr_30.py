class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        has_loop = False
        
        # Detect loop using Floyd's algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_loop = True
                break
        
        if not has_loop:
            return 0
        
        # Count the number of nodes in the loop
        count = 1
        ptr = slow.next
        while ptr != slow:
            ptr = ptr.next
            count += 1
        
        return count
