#coding=utf-8

import datetime
import random
import sys
sys.setrecursionlimit(10000000) 

def timer(func):
	def wrapper(self, paras):
		start_time = datetime.datetime.now()
		process = func(self, paras)
		end_time = datetime.datetime.now()
		delt = end_time - start_time
		print "执行时间为:", delt 
		return process
	return wrapper

class Sort_algorithms(object):
	

###################################插入排序#################################################
	@timer
	def insert_sort_first(self, arr):   

		for index,number in enumerate(arr):
			if number < arr[index-1]:
				pre_index = index - 1 
				while pre_index >= 0:
					if arr[pre_index] > number:
						arr[pre_index], arr[pre_index+1] = arr[pre_index+1], arr[pre_index]
						pre_index = pre_index -1
					else:
						break
	
	@timer
	def insert_sort_second(self, arr):

		length = len(arr)
		for i in range(length):		
			if arr[i] < arr[i-1]:
				number = arr[i]
				j = i - 1
				while number < arr[j] and j >= 0:
					arr[j+1] = arr[j]
					j -= 1
				arr[j+1] = number

	@timer
	def shell_sort(self, arr):
		length = len(arr)
		incerment = length
		while incerment > 1:
			incerment = incerment/4 + 1
			for i in range(incerment, length):
				if arr[i] < arr[i - incerment]:
					number = arr[i]
					j = i - incerment
					while number > arr[j] and j >=0:
						arr[j+incerment] = arr[j]
						j -= incerment
					arr[j+incerment] = number


###################################选择排序#################################################
	@timer
	def direct_select_sort(self, arr):
		length = len(arr)
		for i in range(length):
			min_index = i
			for j in range(i+1, length):
				if arr[j] < arr[min_index]:
					min_index = j
			arr[min_index], arr[i] = arr[i], arr[min_index]

	@timer
	def double_select_sort(self, arr):
		length = len(arr)
		for i in range(0, length/2):
			min_index = i
			max_index = length - i - 1
			for j in range(i + 1, length - i -1):
				if arr[j] < arr[min_index]:
					min_index = j
				elif arr[j] > arr[max_index]:
					max_index = j
			arr[i], arr[min_index] = arr[min_index], arr[i]
			arr[length - i - 1], arr[min_index] = arr[max_index], arr[length - i - 1]

	@timer
	def heap_sort(self, arr):

		def creat_heap_tree(arr):
			length = len(arr)
			top_index = length - 1
			for index in reversed(range(length/2)):
				adjust_node(index, arr, top_index)

		def adjust_node(index, arr, top_index):
			left = index * 2 + 1
			right = left + 1
			while left <= top_index:
				if right <= top_index:
					if arr[right] < arr[left]:
						com_index = right
					else:
						com_index = left
				else:
					com_index = left

				if arr[index] > arr[com_index]:
					arr[index], arr[com_index] = arr[com_index], arr[index]
					index = com_index
					left = index * 2 + 1
					right = left + 1
				else:
					break
		
		def heap_sort(arr):
			
			length = len(arr)
			creat_heap_tree(arr)
			print "the heap list: ", arr
			for end_index in range(length-1, 0,-1):
				arr[end_index], arr[0] = arr[0], arr[end_index]
				adjust_node(0, arr, end_index-1)

			print "the sort list: ", arr

		heap_sort(arr)
		

###################################交换排序#################################################

	@timer
	def bubble(self, arr):
		length = len(arr)
		for end_index in range(length-1, 0, -1):
			for index in range(end_index):
				if arr[index] > arr[index+1]:
					arr[index], arr[index+1] = arr[index+1], arr[index]
		print "the sort list: ", arr

	# @timer
	# def quick_sort(self, arr):

	# 	length = len(arr)

	# 	def sort(arr, start_index=0, end_index = length):
			
	# 		if start_index < end_index:
	# 			current = start_index
	# 			key = arr[start_index]
	# 			for i in range(start_index + 1, end_index):
	# 				if arr[i] < key:
	# 					if i > current + 1:
	# 						arr[i], arr[current + 1] = arr[current + 1], arr[i]
	# 						arr[current + 1], arr[current] =  arr[current], arr[current + 1]
	# 					else:
	# 						arr[i], arr[current] = arr[current], arr[i]
	# 					current = current + 1
	# 			sort(arr, start_index = start_index, end_index = current)
	# 			sort(arr, start_index = current + 1, end_index = end_index)
	# 	sort(arr)
	# 	print arr


	@timer
	def quick_sort(self, arr):
		length = len(arr)
		def sort(arr, start_index=0, end_index=length):
			if start_index < end_index:
				key = arr[start_index]
				current = start_index
				for i in range(start_index + 1, end_index):
					if arr[i] < key:
						if i > current + 1:
							arr[i], arr[current + 1] = arr[current + 1], arr[i]
							arr[current], arr[current + 1] = arr[current + 1], arr[current]
						else:
							arr[i], arr[current] = arr[current], arr[i]
						current = current + 1
				sort(arr, start_index, current)
				sort(arr, current+1, end_index)
		sort(arr)


###################################归并排序#################################################

		
			

list_num = []
for i in range(10):
	list_num.append(random.randint(10,1000))
print "The " + str(len(list_num)) + "_list_num has been created!"
print "the unsort list: ",list_num

test = Sort_algorithms()
# test.insert_sort_second(list_num)
# test.shell_sort(list_num)
# test.direct_select_sort(list_num)
# test.double_select_sort(list_num)
# test.heap_sort(list_num)
# test.bubble(list_num)
# test.quick_sort(list_num)
test.merge_sort(list_num)
print list_num
