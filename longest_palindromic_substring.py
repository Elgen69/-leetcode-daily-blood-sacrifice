# LeetCode Problem #5: Longest Palindromic Substring
# Language: Python
# Technique: Expand Around Center (O(n^2))

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Helper function to expand around a center and return longest palindrome found
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Keep expanding outward as long as characters match
                left -= 1
                right += 1
            # Return the substring (note: left and right are now one step too far)
            return s[left + 1:right]

        # Initialize variable to keep track of longest palindrome
        longest = ""

        # Loop through each character as a potential center
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (single center)
            odd_pal = expand_around_center(i, i)

            # Case 2: Even-length palindrome (center is between two characters)
            even_pal = expand_around_center(i, i + 1)

            # Pick the longer of the two
            current_longest = odd_pal if len(odd_pal) > len(even_pal) else even_pal

            # Update if this is the longest so far
            if len(current_longest) > len(longest):
                longest = current_longest

        return longest

# Example test
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(s.longestPalindrome("cbbd"))   # Output: "bb"
