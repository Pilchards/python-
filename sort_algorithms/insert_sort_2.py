#coding=utf-8
import date


sort = timer(sort)


def timer(func):
	def wrapper():
		start_time = datetime.datetime.now()
		process = func(self, arr)
		end_time = datetime.datetime.now()
		print "执行用时: ", (end_time - start_time)
		return process
	return wrapper

class Sort(object):

	