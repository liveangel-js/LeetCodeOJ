# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'LeetCodeOJ'

f = open("file.txt",'r')

def judge(s):
    s = s.strip()
    list = s.split('-')
    if list[0].isdigit():
        for i in list[1:]:
            if i.isdigit()==False:
                return False
        return True
        # the first is digit
    else:
        a = list[0].split(' ')
        if len(a)!=2:
            return False
        else:
            a[0] = a[0].strip()
            a[1] = a[1]
            if a[0].startswith('(') and a[0].endswith(')'):
                temp = a[1:len(a[0])-1]
                temp = ''.join(temp)
                if temp.isdigit()==False:
                    return False
                else:
                    if a[1].isdigit():
                        return True
                    else:
                        return False
            else:
                return False




for i in f.readlines():
    if judge(i):
        print i.strip()


