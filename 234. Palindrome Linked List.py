#234. Palindrome Linked List
#https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        l=0
        r=len(a)-1
        while l<r:
            if a[l]!=a[r]:
                return False
            l+=1
            r-=1
        return True
        
