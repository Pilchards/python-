#coding=utf-8

# def decorator(function):

# 	def de_decorator(arg1, arg2):
# 		print "before!!!" + arg2
# 		function(arg1)
# 		print "after!!!"
# 	return de_decorator

# @decorator
# def be_decorator(funcc):
# 	print "This is func need additional function!!" + funcc



# def main():
# 	be_decorator("123", "123")

# if __name__ == '__main__':
# 	main()

#------------------------------------分割线——————————————————————————————————————————————————
#装饰器方法

# def method_friendly_decorator(method_to_decorate): 
# 	def wrapper(self, lie): 
# 		lie = lie - 3 # very friendly, decrease age even more :-) 
# 		return method_to_decorate(self, lie) 
# 	return wrapper 

# class Lucy(object): 
# 	def __init__(self): 
# 		self.age = 32 

# 	@method_friendly_decorator 
# 	def sayYourAge(self, lie): 
# 		print "I am %s, what did you think?" % (self.age + lie) 

# l = Lucy() 
# l.sayYourAge(-3)

#------------------------------------分割线——————————————————————————————————————————————————

#装饰器生成器
# def decorator_maker(): 
# 	print "I make decorators! I am executed only once: "+\
# 	"when you make me create a decorator." 
	
# 	def my_decorator(func): 
# 		print "I am a decorator! I am executed only when you decorate a function." 

# 		def wrapped(): 
# 			print ("I am the wrapper around the decorated function. " "I am called when you call the decorated function. " "As the wrapper, I return the RESULT of the decorated function.")
# 			return func()
		
# 		print "As the decorator, I return the wrapped function." 
# 		return wrapped

# 	print "As a decorator maker, I return a decorator"

# 	return my_decorator

# @decorator_maker()
# def decorated_function(): 
# 	print "I am the decorated function." 

# # new_decorator = decorator_maker()
# # decorated_function = new_decorator(decorated_function)

# # decorated_function = decorator_maker()(decorated_function)
# # print "\n"

# decorated_function()

#------------------------------------分割线——————————————————————————————————————————————————

#装饰器生成器
def decorator_maker(arg1, arg2): 
	print "I make decorators with parament! I am executed only once: "+\
	"when you make me create a decorator." +\
	arg1 + arg2 + "\n"
	
	def my_decorator(func): 
		print "I am a decorator! I am executed only when you decorate a function." + "\n" + arg1 + arg2

		def wrapped(func_para): 
			print ("I am the wrapper around the decorated function. " "I am called when you call the decorated function. " "As the wrapper, I return the RESULT of the decorated function." + "\n")
			return func(func_para)
		
		print "As the decorator, I return the wrapped function." + "\n"
		return wrapped

	print "As a decorator maker, I return a decorator" + "\n"

	return my_decorator

# @decorator_maker("arg1", "arg2")
def decorated_function(func_para): 
	print "I am the decorated function."  + "\n"

new_decorator = decorator_maker("arg1","arg2")
print new_decorator.__closure__
decorated_function = new_decorator(decorated_function)
print decorated_function.__closure__

# decorated_function = decorator_maker()(decorated_function)
# print "\n"

# a = decorated_function("func_para")






#------------------------------------分割线——————————————————————————————————————————————————



# 装饰 装饰器 的装饰器 (好绕.....) 
# def decorator_with_args(decorator_to_enhance): 
# 	""" 
# 	这个函数将作为装饰器使用 
# 	它必须装饰另一个函数 
# 	它将允许任何接收任意数量参数的装饰器 
# 	方便你每次查询如何实现 
# 	""" 

# 	# 同样的技巧传递参数 
# 	def decorator_maker(*args, **kwargs): 

# 		# 创建一个只接收函数的装饰器 
# 		# 但是这里保存了从创建者传递过来的的参数 
# 		def decorator_wrapper(func): 

# 			# 我们返回原始装饰器的结果 
# 			# 这是一个普通的函数，返回值是另一个函数 
# 			# 陷阱：装饰器必须有这个特殊的签名，否则不会生效 
# 			return decorator_to_enhance(func, *args, **kwargs) 
# 		return decorator_wrapper 
# 	return decorator_maker


# # 你创建这个函数是作为一个装饰器，但是给它附加了一个装饰器 
# # 别忘了，函数签名是： "decorator(func, *args, **kwargs)" 
# @decorator_with_args 
# def decorated_decorator(func, *args, **kwargs): 
# 	def wrapper(function_arg1, function_arg2): 
# 		print "Decorated with", args, kwargs 
# 	return func(function_arg1, function_arg2) 
# return wrapper 

# # 然后，使用这个装饰器(your brand new decorated decorator) 
# @decorated_decorator(42, 404, 1024) 
# def decorated_function(function_arg1, function_arg2): 
# 	print "Hello", function_arg1, function_arg2 


# decorated_function("Universe and", "everything")


