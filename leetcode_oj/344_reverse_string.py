#coding coding=utf-8

import datetime


def timer(func):
    def wrapper(self, paras):
        start_time = datetime.datetime.now()
        process = func(self, paras)
        end_time = datetime.datetime.now()
        delt = end_time - start_time
        print "执行时间为:", delt
        return process
    return wrapper

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # S = list(s)
        # length = len(s)
        # for index in range(length/2):
        #     S[length-index-1],S[index] = S[index],S[length-index-1]
        # return "".join(S)
        
        
        # return s[::-1]
        
        return ''.join(list(reversed(s)))


test = Solution()
print test.reverseString("")

