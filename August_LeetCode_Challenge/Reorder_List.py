Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list-s nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        
        list_1 = head
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        list_2 = self.reverse(slow)
        
        
        while list_1:
            temp = list_1.next
            list_1.next = list_2
            if not temp:
                break
            list_1 = temp
            
            temp = list_2.next
            list_2. next = list_1
            list_2 = temp
            
    
    def reverse(self, head):
        
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            
            prev = current
            current = temp
            
        return prev
    
    
        
        
        