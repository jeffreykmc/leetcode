#141. Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2024-03-06
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False
