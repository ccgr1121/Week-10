import math
import time

# def check_prime(num: int, primes):
#     limit = math.sqrt(num)
#     for j in primes:
#         if j*j> num:
#             primes.append(num)
#             return primes
#         elif i % j == 0:
#             break
#     else:
#         primes.append(num)
#         return primes   

# prime_numbers = []
# start = time.time()
# for i in range(2, 30000001):
#     check_prime(i, prime_numbers)

# time_took = time.time() - start

# print("The number of prime numbers is:", len(prime_numbers))
# print("The time taken is:", time_took) 

start = time.time()
def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
print("The number of prime numbers is:",len(primes(2000000000)))
time_took = time.time() - start
print("The time taken is:", time_took) 


# end = time.time()
# time_took = end - start









# begin_seconds = time.time()

# prime_array = []
# prime_array_final = []
# prime_count = 0
# for p in range(2, 2000000001):
#     for i in range(2, int(math.sqrt(p))):
#         if i in prime_array:
#             break
#         elif (p % i) == 0:
#             break
#     else:
#         # print(p)
#         prime_array.append(p)
#         prime_array_final.append(p)
#         prime_count += 1 


# end_seconds = time.time()
# print(prime_array_final)
# print(end_seconds-begin_seconds)
# print(prime_count)