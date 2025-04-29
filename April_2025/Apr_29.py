class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def segregate(self, head):
        # Dummy heads and tails for 0, 1, 2 lists
        zero_head = zero_tail = ListNode(-1)
        one_head = one_tail = ListNode(-1)
        two_head = two_tail = ListNode(-1)
        
        current = head
        while current:
            next_node = current.next
            current.next = None  # Disconnect from the next node
            if current.data == 0:
                zero_tail.next = current
                zero_tail = zero_tail.next
            elif current.data == 1:
                one_tail.next = current
                one_tail = one_tail.next
            else:
                two_tail.next = current
                two_tail = two_tail.next
            current = next_node
        
        # Link the three lists
        # Check if zero list is non-empty
        if zero_head.next:
            result_head = zero_head.next
            # Link zero tail to one list if exists, else two list
            if one_head.next:
                zero_tail.next = one_head.next
                # Link one tail to two list if exists
                if two_head.next:
                    one_tail.next = two_head.next
            else:
                zero_tail.next = two_head.next if two_head.next else None
        elif one_head.next:
            result_head = one_head.next
            # Link one tail to two list if exists
            if two_head.next:
                one_tail.next = two_head.next
        else:
            result_head = two_head.next
        
        return result_head
