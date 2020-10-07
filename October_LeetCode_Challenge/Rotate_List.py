Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# O(n) Time and O(1) Space
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head is None:
            return None
        
        tail = head
        n = 1
        
        while tail.next:
            n += 1
            tail = tail.next
            
        k %= n
        
        if k==0:
            return head
        
        tail.next = head
        current = head
        
        steps = n-k
        while steps-1:
            current = current.next
            steps -= 1
        
        head = current.next
        current.next = None
        return head
        
            