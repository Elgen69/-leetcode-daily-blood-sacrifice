# LeetCode Problem #1: Two Sum
# Language: Python
# Technique: Hashmap (dictionary) for O(n) lookup time

# In Python, we define a class to group methods together (just like a container for logic).
class Solution(object):
    def twoSum(self, nums, target):
        """
        Function to find the indices of two numbers that add up to the target.

        :type nums: List[int]  --> this means nums is expected to be a list of integers
        :type target: int      --> this is the target number we want to get by adding two elements in nums
        :rtype: List[int]      --> this function will return a list with 2 integers (the indices)
        """
        
        # Create an empty dictionary to store numbers we've seen so far
        # The key will be the number, the value will be its index in the list
        seen = {}

        # The enumerate() function gives us both the index and the number at the same time
        for i, num in enumerate(nums):
            # Compute the number we need to reach the target
            complement = target - num

            # Check if we have already seen the complement before
            # If yes, then we found our answer and return the indices
            if complement in seen:
                return [seen[complement], i]

            # If we haven't seen it, store the number and its index for future reference
            seen[num] = i

        # If no solution is found (shouldn't happen as per problem guarantees), return empty list
        return []

# Test code: This runs only if the file is executed directly (not imported)
# It's a good way to try out your function locally.
if __name__ == "__main__":
    # We create an object of the Solution class
    s = Solution()

    # Call the twoSum function with an example input
    result = s.twoSum([2, 7, 11, 15], 9)

    # Print the result to see if it's correct
    print("Indices of numbers that add up to target:", result)  # Expected output: [0, 1]
