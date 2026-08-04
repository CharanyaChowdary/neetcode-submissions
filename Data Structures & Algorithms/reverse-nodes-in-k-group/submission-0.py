class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or head is None:
            return head

        curr = head

        # Check if at least k nodes exist
        for _ in range(k):
            if curr is None:
                return head
            curr = curr.next

        prev = None
        curr = head

        # Reverse first k nodes
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect the remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev