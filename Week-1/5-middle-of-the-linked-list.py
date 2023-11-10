'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

Question: https://leetcode.com/problems/middle-of-the-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 1
        if current.next == None:
            return current

        while current.next != None:
            current = current.next
            length = length + 1
        
        for i in range(int(length/2)):
            head = head.next
        
        return head

'''
Time Complexity: O(n) - 2 passes - though one pass possible
Space Complexity: O(1) - no additional data structure
'''
