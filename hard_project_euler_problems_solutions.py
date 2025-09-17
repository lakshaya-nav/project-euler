def prime(num):
    for i in range(2, int((num**0.5))+1):
        if not num % i:
            return False
    return True

result = 2
for i in range(3,2000000,2):
    if prime(i):
        result += i


import math
def highly_divisible_triangular_no():
    step = 0
    num = 0
    divisors = 0

    while divisors < 500:
        divisors = 0
        step += 1
        num += step
        for n in range(2, int(math.sqrt(num))):
            if num % n == 0:
                divisors += 2

    return num

from itertools import permutations
def lexicographic_permutations():
    vals = list(permutations('0123456789'))
    vals = [''.join(x) for x in vals]
    vals = list(map(int, vals))
    final = sorted(vals)
    return final[999999]




def non_abundant_sums():
    sum = 0
    l = []
    l1 = []
    for n in range(2, 28124):
        sum = 0
        for divisors in range(1, n):
            if n % divisors == 0:
                sum += divisors

        if sum > n:
            l.append(n)


    for i in range(0, len(l)-1):
        for j in range(0, len(l)-1):
            l1.append(l[i] + l[j])
    lis = set(l1)

    sum2 = 0
    for i in range(1, 28124):
        if i not in lis:
            sum2 += i
    return sum2


def reciprocal_cycles():
    longest_recurring_cycle = 0
    for n in range(2, 1001):
        if not any(n % m == 0 for m in range(2, n)):
            fraction = str(1/n)
            count = 1
            if len(fraction) > 15:
                for index, recurring_cycle in enumerate(fraction[3:10]):
                    if recurring_cycle == fraction[2] and recurring_cycle == fraction[index + 3 + count]:
                        break
                    elif count >= longest_recurring_cycle:
                        longest_recurring_cycle = count
                        longest_value = n
                    count += 1
    print(longest_value)


def quadratic_primes():
    primes = []
    max = 0
    product = 0
    for n in range(2, 10000):
        if not any(n % m == 0 for m in range(2, n)):
            primes.append(n)

    for a in range(-1000, 1000):
        print(a)
        for b in range(-1000, 1001):
            count = 0
            for n in range(1000):
                if n**2 + a*n + b in primes:
                    count += 1
                else:
                    if count > max:
                        max = count
                        product = a*b
                    break
    return product

def pandigital_products():
    sum = 0
    product_list = []
    for n in range(1,2000):
        for m in range(1,2000):
            l = []
            product = n*m
            for digit in str(product):
                l.append(int(digit))
            for digit in str(n):
                l.append(int(digit))
            for digit in str(m):
                l.append(int(digit))
            print(l)
            if sorted(l) == [1,2,3,4,5,6,7,8,9] and product not in product_list:
                product_list.append(product)
                sum += product
    return sum

def digit_cancelling_fractions():

    for n in range(10,100):
        for m in range(10,100):
            if n % 10 != 0 and m % 10 != 0 and n<m:
                for i in str(n):
                    for j in str(m):
                        if i == j:
                            remove = i
                            break
                for i in str(n):
                    if i != remove:
                        n1 = i
                for j in str(n):
                    if j != remove:
                        m1 = j
                if n/m == n1/m1:
                    print(n)
                    print(m)

def trunctable_primes():
    primes = []
    sum = 0
    for n in range(2, 800000):
        if not any(n % m == 0 for m in range(2, n)):
            primes.append(n)

    for num in primes:
        num1 = str(num)
        num2 = str(num)
        count = 0
        for digit in range(len(str(num))-1):
            if int(num1[:-1]) in primes and int(num2[1:]) in primes:
                count += 1
            else:
                break
            num1 = num1[:-1]
            num2 = num2[1:]
        if count == len(str(num))-1:
            sum += num
            print(num)
    return sum

def pandigital_multiples():
    l = [1,2,3,4,5,6,7,8,9]
    max = 0

    for n in range(1,100000):
        digits = []
        products = ''
        for i in range(1,10):
            product = n * i
            if len(products) >= 9:
                break
            else:
                products += str(product)
        for digit in products:
            digits.append(int(digit))
        if sorted(digits) == l:
            if int(products) > max:
                max = int(products)

    return max

def pandigital_prime():
    vals = list(permutations('1234567'))
    vals = [''.join(x) for x in vals]
    print(vals)
    max = 0
    for x in vals:
        if x[0] == '7':
            if not any(int(x) % m == 0 for m in range(2, int(x))):
                if int(x) > max:
                    max = int(x)
                    print(max)
    return max

def sub_string_divisibility():
    prime = [2,3,5,7,11,13,17]
    sum = 0
    vals = list(permutations('0123456789'))
    vals = [''.join(x) for x in vals]
    for n in vals:
        a = 1
        b = 3
        count = 0
        for i in range(len(prime)):
            if int(n[a:b+1]) % prime[i] == 0:
                count += 1
                a += 1
                b += 1
            else:
                break
        if count == 7:
            sum += int(n)
    return sum



def prime_permutations():
    for n in range(999, 10000, 2):
        if not any(n % m == 0 for m in range(2, n)):
            lis = list(permutations(str(n)))
            lis = [''.join(x) for x in lis]
            l = []
            for val in lis:
                if not any(int(val) % m == 0 for m in range(2, int(val))):
                    l.append(int(val))
            if len(l) > 2:
                for i in l:
                    for j in l:
                        for k in l:
                            if j-i == k-j and i!=j!=k:
                                print(i,j,k)



def distinct_primes_factors():
    l = [2]
    four_distinct_primes = []
    for n in range(3, 150000, 2):
        print(n)
        if not any(n % m == 0 for m in range(2, n)):
            l.append(n)

    for i in range(9000, 150000):
        print(i)
        index = 0
        count = 0
        for j in l:
            if j > i:
                index = l.index(j)
        leftover = i
        for k in l[:index]:
            if leftover % k == 0:
                count += 1
                leftover = leftover / k
        if count == 4:
            four_distinct_primes.append(i)
    print(four_distinct_primes)

    for idx in range(len(four_distinct_primes)-4):
        print(four_distinct_primes[idx])
        if four_distinct_primes[idx] + 3 == four_distinct_primes[idx+1] + 2 ==  four_distinct_primes[idx+2] + 1 == four_distinct_primes[idx+3]:
            return four_distinct_primes[idx]


def coin_sums():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * target
    print(ways)

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
            print(ways[i])
    return ways[target]


def digit_cancelling_fractions():
    numerator = 1
    denominator = 1
    for i in range(10, 100):
        for j in range(10, 100):
            l1 = []
            l2 = []
            if i < j and i != j:
                fraction = i/j
                for digit1 in str(i):
                    l1.append(digit1)
                for digit2 in str(j):
                    l2.append(digit2)
                common = list(set(l1) & set(l2))
                if len(common) == 1:
                    if common[0] != '0':
                        l1.remove(common[0])
                        l2.remove(common[0])
                    if l2[0] != '0':
                        if fraction == int(l1[0]) / int(l2[0]):
                            if i % 10 != 0:
                                numerator *= i
                                denominator *= j
    return numerator / denominator

def pentagon_numbers():
    pentagon = []
    for n in range(1000, 5000):
        pentagon.append(int(n * (3 * n - 1) / 2))
    print(pentagon)
    for i in pentagon:
        for j in pentagon:
            if i > j and i + j in pentagon and i - j in pentagon:
                print(i, j)



