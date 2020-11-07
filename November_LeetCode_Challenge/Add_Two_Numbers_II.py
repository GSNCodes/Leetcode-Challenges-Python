You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My Solution

# O(n) Time and O(n) Space
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def helper(l_list):
            
            head = l_list
            result = 0
            while head is not None:
                result = result*10 + head.val
                head = head.next
                
            return result
        
        combined_sum = helper(l1) + helper(l2)
        
        result_list = ListNode(int(str(combined_sum)[0]))
        head = result_list
        for char in str(combined_sum)[1:]:
            result_list.next = ListNode(int(char))
            result_list = result_list.next
        
        return head
            
        
        
        
            
            