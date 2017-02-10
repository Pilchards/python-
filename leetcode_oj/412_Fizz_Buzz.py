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

    @timer
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # queue_list = []
        # for number in range(1,n+1):
        #     if number%3 == 0:
        #         if number%5 == 0:
        #             queue_list.append("FizzBuzz")
        #             continue
        #         queue_list.append("Fizz")
        #         continue
        #     if number%5 == 0:
        #         queue_list.append("Buzz")
        #     else:
        #         queue_list.append(str(number))
        # return queue_list 

######################################分割线########################################################

        return [[[str(number),"Fizz"],["Buzz","FizzBuzz"]][number%5==0][number%3==0] for number in range(1, n+1)]

######################################分割线########################################################

        # list_all = []
        # for i in range(0,n/15+1):
        #     list_all.append(str(1+i*15))
        #     list_all.append(str(2+i*15))
        #     list_all.append("Fizz")
        #     list_all.append(str(4+i*15))
        #     list_all.append("Buzz")
        #     list_all.append("Fizz")
        #     list_all.append(str(7+i*15))
        #     list_all.append(str(8+i*15))
        #     list_all.append("Fizz")
        #     list_all.append("Buzz")
        #     list_all.append(str(11+i*15))
        #     list_all.append("Fizz")
        #     list_all.append(str(13+i*15))
        #     list_all.append(str(14+i*15))
        #     list_all.append("FizzBuzz")
        
        # for i in range(0,15-n%15):
        #     del list_all[-1]
    
        # return list_all

a = Solution()
b = a.fizzBuzz(50000)
# print b