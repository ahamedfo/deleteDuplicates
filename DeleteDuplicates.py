# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        tempHead = head
        walker = head
        while head.next != None:

            k = tempHead.next
            if k.val != tempHead.val:
                head.next = tempHead.next
                head = head.next
            elif k.val == tempHead.val and k.next == None:
                print (tempHead)
                head.next = None
                print (tempHead)

            tempHead = tempHead.next
        return walker
        """
        :type head: ListNode
        :rtype: ListNode
        """
