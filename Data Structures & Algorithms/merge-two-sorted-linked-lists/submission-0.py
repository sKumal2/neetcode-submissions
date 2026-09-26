# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #since we need O(1) space we cannot use a new array to add the lists and sort it, so we use something intelligent called dummy
        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            #compare the nodes of list1 and list2 and add it to tail
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 

            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next