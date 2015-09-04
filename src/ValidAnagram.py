# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'LeetCodeOJ'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts={}
        for i in s:
            if dicts.get(i)==None:
                dicts[i]=1
            else:
                dicts[i]=dicts[i]+1
        dictt={}
        for j in t:
            if dictt.get(j)==None:
                dictt[j]=1
            else:
                dictt[j]=dictt[j]+1

        if cmp(dicts,dictt)==0:
            return True
        else:
            return False


solution = Solution()
print solution.isAnagram("anagram","nagaram")