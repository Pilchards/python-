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
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


test = Solution()
print test.singleNumber()