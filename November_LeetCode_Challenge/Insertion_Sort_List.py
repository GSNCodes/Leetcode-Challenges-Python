Sort a linked list using insertion sort.
Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# My Solution
# O(n^2) Time and O(1) Space
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        if not head:
            return 
        
        
        dummy = ListNode()
        dummy.next = head
        
        current = head
        
        while current:
            
            if current.next and current.next.val < current.val:
                
                temp = current.next
                current.next = current.next.next
                insert = dummy
                while insert.next.val < temp.val:
                    insert = insert.next
                
                temp.next = insert.next
                insert.next = temp
            
            else:
                current = current.next
                
        return dummy.next