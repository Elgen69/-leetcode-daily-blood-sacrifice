# Definition for singly-linked list (LeetCode gives you this already)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val  # The digit stored in this node
        self.next = next  # The reference to the next node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Create a dummy head node (a placeholder so we can build the result list easily)
        dummy_head = ListNode(0)

        # This is the current node we're working with in the result list
        current = dummy_head

        # This keeps track of the carry (like when 9+9 = 18, you carry over 1)
        carry = 0

        # Loop through both lists until we reach the end of both
        while l1 or l2 or carry:
            # Get current values; if one list is shorter, use 0 as its value
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the digits plus any carry from previous addition
            total = val1 + val2 + carry

            # Update carry for next digit (if total is 15, carry will be 1)
            carry = total // 10  # Integer division
            new_digit = total % 10  # Remainder is the digit to store

            # Create a new node with the result digit and attach it to result list
            current.next = ListNode(new_digit)

            # Move to the next node in result list
            current = current.next

            # Move to the next nodes in l1 and l2 if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next node after dummy (the real head of our result list)
        return dummy_head.next

# Example: Building the linked lists manually and testing
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def build_list(values):
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to print linked list
    def print_list(node):
        result = []
        while node:
            result.append(str(node.val))
            node = node.next
        print(" -> ".join(result))

    # Example 1: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print("Result:")
    print_list(result)  # Output: 7 -> 0 -> 8
