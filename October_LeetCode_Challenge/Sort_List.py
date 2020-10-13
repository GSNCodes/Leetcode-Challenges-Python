Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My Solution
# O(nlogn) Time and O(logn) Space
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        prev=None
        slow=head
        fast=head
        
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, list_1, list_2):
        
        temp = ListNode(-1)
        current = temp
        
        while list_1 is not None and list_2 is not None:
            if list_1.val < list_2.val:
                current.next = list_1
                list_1 = list_1.next
            
            else:
                current.next = list_2
                list_2 = list_2.next
                
            current = current.next
            
        current.next = list_1 if list_1 is not None else list_2
        
        return temp.next




# O(nlogn) Time and O(n) Space
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        node_list.sort()
        head = p
        for i in node_list:
            head.val = i
            head = head.next

        return p