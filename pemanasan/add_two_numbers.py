# Leetcode add two numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def list_to_linked(lst):
        dummy = ListNode(0)
        curr = dummy
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)