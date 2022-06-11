"""
3Sum
=================

https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution(object):
    def threeSum_Helper(self, num, nums):
        result = []
        target = -1 * num
        l, r = 0, len(nums)-1
        while l < r:
            sum_lr = nums[l] + nums[r]
            if sum_lr == target:
                result.append([num, nums[l], nums[r]])
                last_l = nums[l]
                while nums[l] == last_l and l < r:
                    l += 1
                last_r = nums[r]
                while nums[r] == last_r and r > l:
                    r -= 1
            elif sum_lr < target:
                l += 1
            else:
                r -= 1
                
        return result

    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        nums = sorted(nums)
        
        for i in range(0, len(nums)):
            triplets = self.threeSum_Helper(nums[i], nums[:i:])
            if triplets:
                for triplet in triplets:
                    triplet = sorted(triplet)
                    if triplet and triplet not in result:
                        result.append(triplet)
        
        return result
    
    """
    Brute Force:
    def threeSum(self, nums):
        result = []
        
        for i in range(0, len(nums) - 2):
            #print(nums[i])
            for j in range(i + 1, len(nums) - 1):
                #print(f"\t{nums[j]}")
                for k in range(j + 1, len(nums)):
                    #print(f"\t\t{nums[k]}")
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
        
        return result
    """
