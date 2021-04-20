Explaination: https://www.youtube.com/watch?v=V73kvNdbEvg
https://www.youtube.com/watch?v=OEufAMjQ62c

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def digitNum(head):
            s=''
            while head:
                s= s+str(head.val)
                head = head.next
            return s[::-1]
        
        def createLinkedList(head, v):
            if head.val==0:
                head.val = v
                head.next = None
                return head
            else:
                ptr = head
                while ptr.next is not None:
                    ptr = ptr.next
                node = ListNode()
                node.val = v
                node.next = None
                ptr.next = node
                return head
            
        
        sm = int(digitNum(l1)) + int(digitNum(l2))
        
        sm = str(sm)[::-1]
        
        head = ListNode()
        
        for v in sm:
            head = createLinkedList(head, v)
        return head