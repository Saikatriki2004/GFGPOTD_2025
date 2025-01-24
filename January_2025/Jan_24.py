class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize two pointers, slow and fast.
        slow = head
        fast = head

        while fast and fast.next:
            # Move slow pointer one step.
            slow = slow.next
            # Move fast pointer two steps.
            fast = fast.next.next

            # If slow and fast meet, there is a loop.
            if slow == fast:
                return True

        # If we reach here, there is no loop.
        return False
