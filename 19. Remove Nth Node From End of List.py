#19. Remove Nth Node From End of List

#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #a=[]*n
        b=c=d=ListNode("sentienel",head)
        b=c=d=head
        a=1
        while d.next != None:
            #print(a,)
            if a>=n:
                b=c.next
                c=d.next
                print('move',a)
            else:
                a+=1
            #a.append(c.next)
            #print('a',a)
            d=d.next
        
        
        b=c.next.next
        #b=b.next
        print(b)
        print(head)

        return head
        


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next
       
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next




    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #a=[]*n
        b=c=d=e=ListNode(0)
        d.next=head
        b=c=e=d.next
        a=0
        while d.next is not None:
            #print(a,)
            if a>n+1:
                b=c.next
                c=c.next
                print('move',a)
            else:
                a+=1
                #b=d.next
                c=d
            #a.append(c.next)
            #print('a',a)
            #print('a',b)
            d=d.next
        
        
        b=c.next.next
        #b=b.next
        #print(b)


        return e