import math
import time


start = time.time()
def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
print("The number of prime numbers is:",len(primes(3000000)))
time_took = time.time() - start
print("The time taken is:", time_took) 








# def check_prime(num: int, primes):

#     for j in primes:
#         if j*j > num:
#             primes.append(num)
#             return primes
#         elif i%j==0:
#             return primes
#     else:
#         primes.append(num)
# prime_numbers = []
# start = time.time()
# for i in range(3, 3000001, 2):
#     check_prime(i, prime_numbers)
# time_took = time.time() - start
# print("The number of prime numbers is:", len(prime_numbers))
# print("The time taken is:", time_took) 







# begin_seconds = time.time()

# prime_array = []
# prime_count = 0
# for p in range(2, 3000001):
#     for i in range(2, int(math.sqrt(p))):
#         if (p % i) == 0:
#             break
#     else:
#         prime_array.append(p)
#         prime_count += 1 

# end_seconds = time.time()
# print(prime_array)
# print(end_seconds-begin_seconds)
# print(prime_count)

