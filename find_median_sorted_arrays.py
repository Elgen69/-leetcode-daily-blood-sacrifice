# LeetCode Problem #4: Median of Two Sorted Arrays
# Language: Python
# Technique: Merge + Median finding (O(m + n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Step 1: Merge the two sorted arrays into one sorted array
        merged = []
        i, j = 0, 0  # pointers for nums1 and nums2

        # Merge process — similar to the merge step of merge sort
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add remaining elements (if any) from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Add remaining elements (if any) from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Step 2: Find the median
        n = len(merged)

        if n % 2 == 1:
            # Odd number of elements — middle one is the median
            return float(merged[n // 2])
        else:
            # Even number of elements — average of two middle ones
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0

# Example test (remove before submitting if needed)
if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))         # Output: 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))      # Output: 2.5
