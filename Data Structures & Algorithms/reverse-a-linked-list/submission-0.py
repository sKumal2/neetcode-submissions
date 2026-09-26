# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we can use brute force but it would take O(n) time and space, but we need O(1) space and O(n) time. 

        curr = head 
        prev = None

        while curr:
            #save the next node
            next_node = curr.next
            #point the current.next to prev
            curr.next = prev 
            prev = curr
            curr = next_node

        return prev
