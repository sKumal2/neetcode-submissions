# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #edge cases: 
        #removing head, so need dummy 

        #using first pointer so we can move it n steps forward, 
        #and moving second pointer and first together until first reaches None 
        #second is right before the node we want to remove coz we point it to dummy and not head, now we can remove the next node and return the list 

        dummy = ListNode(0, head)
        first = head 

        for i in range(n):
            first = first.next 

        second = dummy

        while first:
            first = first.next 
            second = second.next 

        second.next = second.next.next

        return dummy.next

