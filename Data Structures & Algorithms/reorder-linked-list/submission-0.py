# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #concept: reorder the linkedlist based on the pattern given
        #pattern = [0, n-1, 1, n-2, 2, n-3]
        #Example = [0, 1, 2, 3, 4, 5, 6]
        #Output = [0, 6, 1, 5, 2, 4, 3]

        #problem: we have to move from first node to last, last to second, and cont... which takes a lot of time 
        #possible approach: split into two linkedlist, one starting from first, and other starting from last(reverse linkedlist)
        #then combine them later 
        #In order to do that, we need to introduce two pointers, slow and fast pointer

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #introduce second pointer so it becomes another linkedlist with head second and break the first one 
        second = slow.next 
        slow.next = None

        #now we need to reverse second linked list 
        prev = None 

        while second:
            #save next node 
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp

        #after reversing, second = None

        #now since we have two linkedlists, one with head second, use first as head then merge both according to pattern 

        first = head
        second = prev #as the head is stored here, we also return prev when reversing the linked list

        while second:
            #introducing temp so it will be easier
            temp1 = first.next 
            temp2 = second.next 

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        return


