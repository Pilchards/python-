#coding=utf-8

class decoratorWithoutArguments(object):  
  
    def __init__(self, f):  
        """ 
        If there are no decorator arguments, the function 
        to be decorated is passed to the constructor. 
        """  
        print "Inside __init__()"  
        self.f = f  
  
    def __call__(self, *args):  
        """ 
        The __call__ method is not called until the 
        decorated function is called. 
        """  
        print "Inside __call__()"  
        self.f(*args)  
        print "After self.f(*args)"  
 
@decoratorWithoutArguments  
def sayHello(a1, a2, a3, a4):  
    print 'sayHello arguments:', a1, a2, a3, a4  
  
print "After decoration"  
#这种装饰器会在__init__会被调用一次，每次调用时候都会调用__call__  

print "\nPreparing to call sayHello()"  
sayHello("say", "hello", "argument", "list")  

print "\nAfter first sayHello() call"  
sayHello("a", "different", "set of", "arguments")  
# print "After second sayHello() call"  
