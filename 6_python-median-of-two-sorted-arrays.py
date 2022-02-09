"""
Median of Two Sorted Arrays
===========================

https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def mergeArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        while(len(nums1) > 0 and len(nums2) > 0):
            if nums1[0] < nums2[0]:
                nums3.append(nums1[0])
                nums1.pop(0)
            elif nums2[0] < nums1[0]:
                nums3.append(nums2[0])
                nums2.pop(0)
            else:
                nums3.append(nums1[0])
                nums3.append(nums2[0])
                nums1.pop(0)
                nums2.pop(0)
        while(len(nums1) > 0):
            nums3.append(nums1[0])
            nums1.pop(0)
        while(len(nums2) > 0):
            nums3.append(nums2[0])
            nums2.pop(0)
        return nums3
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = self.mergeArrays(nums1, nums2)
        if len(nums3) % 2 == 1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[(len(nums3)//2)-1]+nums3[len(nums3)//2])/2