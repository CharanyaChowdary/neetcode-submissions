# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        temp=head
        while temp is not None:
            temp=temp.next
            length+=1
        if length==n:
            t=head
            head=head.next
            t.next=None
            return head
        index=length-n
        temp1=head
        for i in range(1,index):
            temp1=temp1.next
        r=temp1.next
        t=r.next
        r.next=None
        temp1.next=t
        return head

        
        