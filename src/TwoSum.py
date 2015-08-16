# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'LeetCodeOJ'
import copy

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        if(nums == None or len(nums)<2):
            return None

        dic = {}
        for index in range(0, len(nums)):
            dic[nums[index]]= index+1
        print dic
        for i in range(0, len(nums)):

            index1 = i+1
            if target-nums[i] in dic:
                index2 = dic[target-nums[i]]
                if index1 == index2:
                    continue
                else:
                    return index1, index2

solution = Solution()
print solution.twoSum([0,-2,-3,-4,0], 0)