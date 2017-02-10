#coding=utf-8

import math

def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0:
				return False
		return True
	return False

def get_prime(start):
	each_number = start + 1
	while True:
		if is_prime(each_number):
			print each_number
			yield each_number
			return
		each_number = each_number + 1

def simple_generator_function():
	yield 1
	yield 2
	yield 3

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
            print type(number), number
        number += 1

def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))


def main():
	# a = get_prime(100)
	# while True:
	# 	next(a)
	prime_generator = get_primes(10)
	a = prime_generator.send(None)
	print a
	b = prime_generator.send(103)
	print b




if __name__ == '__main__':
	main()