# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        anslist = ListNode(0)
        anslisthead = anslist
        while(l1!=None or l2!=None):
            s = 0
            if l1!=None:
                s+=l1.val
            if l2!=None:
                s+=l2.val
            s = s + carry
            carry = s/10
            anslisthead.next =  ListNode(s%10)
            anslisthead=anslisthead.next
            if l1!=None:
                l1= l1.next
            if l2!=None:
                l2 = l2.next
        if carry !=0:
            anslisthead.next = ListNode(carry)
        return anslist.next
