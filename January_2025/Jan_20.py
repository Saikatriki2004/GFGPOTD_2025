# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        # Create a dummy node to serve as the start of the merged list
        dummy = Node(0)
        current = dummy

        # Merge the two lists
        while head1 and head2:
            if head1.data <= head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        # Attach the remaining nodes from the non-empty list
        if head1:
            current.next = head1
        if head2:
            current.next = head2

        # Return the merged list, skipping the dummy node
        return dummy.next
