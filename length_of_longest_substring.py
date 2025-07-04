# LeetCode Problem #3: Longest Substring Without Repeating Characters
# Language: Python
# Technique: Sliding Window + Set

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # A set to keep track of characters in the current window (no duplicates allowed)
        seen_chars = set()

        # Left and right are two pointers that define our sliding window
        left = 0
        max_length = 0  # Stores the length of the longest valid substring

        # Right pointer moves one character at a time
        for right in range(len(s)):
            # If we see a duplicate character, we shrink the window from the left
            while s[right] in seen_chars:
                seen_chars.remove(s[left])  # remove the leftmost character
                left += 1  # move the left pointer forward

            # Add the new character to the set
            seen_chars.add(s[right])

            # Update the max_length if current window is larger
            max_length = max(max_length, right - left + 1)

        return max_length

# Example test code for manual runs (remove for submission)
if __name__ == "__main__":
    s = Solution()
    test_input = "abcabcbb"
    print("Length of longest substring:", s.lengthOfLongestSubstring(test_input))  # Output: 3
