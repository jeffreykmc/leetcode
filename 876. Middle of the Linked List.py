#876. Middle of the Linked List
#https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        while head and head.next:
            head=head.next.next
            a=a.next
        return a
