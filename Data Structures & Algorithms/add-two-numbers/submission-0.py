# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = None
        carry = 0
        while (l1 is not None) and (l2 is not None):
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            if res is None:
                res = ListNode()
                curr = res
            else:
                prev = curr
                curr = ListNode()
                prev.next = curr
            curr.val = val
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            val = l1.val + carry
            carry = val // 10
            val = val % 10
            if res is None:
                res = ListNode()
                curr = res
            else:
                prev = curr
                curr = ListNode()
                prev.next = curr
            curr.val = val
            l1 = l1.next
        while l2 is not None:
            val = l2.val + carry
            carry = val // 10
            val = val % 10
            if res is None:
                res = ListNode()
                curr = res
            else:
                prev = curr
                curr = ListNode()
                prev.next = curr
            curr.val = val
            l2 = l2.next
        if carry != 0:
            prev = curr
            curr = ListNode()
            curr.val = carry
            prev.next = curr
        return res
            