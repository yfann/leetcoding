#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
import math
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to hold the result
        dummy = ListNode()
        # Create a pointer to the dummy node
        pointer = dummy
        # Create a carry variable to hold the carry
        carry = 0

        # Loop through the linked list until both are empty
        while l1 or l2:
            # Get the value of the current node in l1
            val1 = l1.val if l1 else 0
            # Get the value of the current node in l2
            val2 = l2.val if l2 else 0
            # Calculate the sum of the two values and the carry
            total = val1 + val2 + carry
            # Calculate the carry
            carry = total // 10
            # Create a new node with the value of the total
            pointer.next = ListNode(total % 10)
            # Move the pointer to the next node
            pointer = pointer.next
            # Move the pointers of the linked lists to the next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there is a carry left, create a new node with the value of the carry
        if carry:
            pointer.next = ListNode(carry)

        # Return the next node of the dummy node
        return dummy.next



# @lc code=end

