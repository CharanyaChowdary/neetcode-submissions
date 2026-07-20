# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle using fast and slow pointer
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        l2=temp
        #reverse 2nd half
        before=None
        curr=l2
        while curr:
            temp=curr.next
            curr.next=before
            before=curr
            curr=temp
        #reorder 
        temp1=head
        temp2=before
        while temp2:
            x=temp1.next
            temp1.next=temp2
            y=temp2.next
            temp2.next=x
            temp1=x
            temp2=y
        

               
        
        
            
        