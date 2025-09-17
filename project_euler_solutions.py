def multiple_of_3_or_5(maximum):
    sum = 0
    extra = 0
    for n in range(1, maximum):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum

def even_fibonacci_no(term1, term2):
    l = [term1, term2]
    sum = 0
    while term1 + term2 < 4000000:
        term3 = term1 + term2
        l.append(term3)
        term1 = term2
        term2 = term3

    for n in l:
        if n % 2 == 0:
            sum += n

    return sum

def largest_prime_factor(number):
    max = 0
    for n in range(2, number+1):
        if not any(n % m == 0 for m in range(2, n)):
            if number % n == 0 and max < n:
                max = n
                print(max)

    return max

def is_palindrome(number):
    return int(str(number)[::-1])

def largest_palindrome_product():
    maximum = 0
    for n in range(100, 1000):
        for num in range(100, 1000):
            product = n * num
            if is_palindrome(product) == product:
                if maximum < product:
                    maximum = product
    return maximum

def find_factorial(num):
    factorial = 1
    for n in range(1, num+1):
        factorial = n * factorial
    return factorial

def smallest_multiple(num1):
    count = 0
    for n in range(0, find_factorial(num1)+1):
        for num in range(1, num1+1):
            if n % num == 0:
                count += 1
                if count == num1:
                    return n
            else:
                count = 0
                break

# smallest_multiple(600851475143)

# def smallest_multiple2(number):
#     for i in range(2, 21):
#         if number % i != 0:
#             return False
#     return True
#
# number = 20
# while True:
#     if smallest_multiple2(number):
#         break
#     number += 20
#
# print(number)

def sum_square_difference(num):
    sum = 0
    sum_of_square = 0
    for n in range(1, num + 1):
        sum_of_square += n**2
        sum += n

    square_of_sum = sum**2
    return square_of_sum - sum_of_square

def prime():
    count = 0
    for n in range(2, 1000000):
        if not any(n % m == 0 for m in range(2, n)):
            num = n
            count += 1
        if count > 10000:
            break
    return num



def special_pythagorean_triplet():
    for a in range(1, 999):
        for b in range (1, 999):
            for c in range (1, 999):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a*b*c

def largest_product_in_series(nums):

    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    l = [int(i) for i in str(num)]
    maximum = 0
    for i in range(0, len(l)-12):
        product = 1
        for n in range(0, nums):
            product *= l[i+n]
            print(product)
        if product > maximum:
            maximum = product
            print(maximum)
    return l, maximum

def summation_of_primes():
    num = 0
    for n in range(2, 100000):
        if not any(n % m == 0 for m in range(2, n)):
            num += n
            print(n)
        if n > 2000000:
            break
    return num

def largest_product_in_a_grid():
    matrix = [[8, 2, 22, 97, 38, 15, 0, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
     [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
     [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
     [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
     [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
     [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
     [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
     [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
     [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
     [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
     [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
     [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
     [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
     [19, 80, 81, 68, 0, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
     [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
     [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
     [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
     [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
     [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
     [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

    l = []
    for row in matrix:
        for i in range(0, len(row)-3):
            left = row[i]*row[i+1]*row[i+2]*row[i+3]
            l.append(left)

    for i in range(0, len(matrix)-1):
        for row in range(0, len(matrix)-3):
            down = matrix[row][i]*matrix[row+1][i]*matrix[row+2][i]*matrix[row+3][i]
            l.append(down)

    for row in range(0, len(matrix)-3):
        for i in range(0, len(matrix)-3):
            diagonal = matrix[row][i] * matrix[row + 1][i + 1] * matrix[row + 2][i + 2] * matrix[row + 3][i + 3]
            l.append(diagonal)

    for row in range(19, len(matrix)-16, -1):
        for i in range(0, len(matrix)-3):
            diagonal2 = matrix[row][i] * matrix[row - 1][i + 1] * matrix[row - 2][i + 2] * matrix[row - 3][i + 3]
            l.append(diagonal2)

    return max(l)

def highly_divisible_triangular_no():
    total = 0
    divisors = 0
    n = 0
    while True:
        n += 1
        divisors = 0
        total += n
        for i in range(1, total+1):
            if total % i == 0:
                divisors += 1

        if divisors > 500:
            break
    return total

def large_sum():
    l = [37107287533902102798797998220837590246510135740250,
    46376937677490009712648124896970078050417018260538,
    74324986199524741059474233309513058123726617309629,
    91942213363574161572522430563301811072406154908250,
    23067588207539346171171980310421047513778063246676,
    89261670696623633820136378418383684178734361726757,
    28112879812849979408065481931592621691275889832738,
    44274228917432520321923589422876796487670272189318,
    47451445736001306439091167216856844588711603153276,
    70386486105843025439939619828917593665686757934951,
    62176457141856560629502157223196586755079324193331,
    64906352462741904929101432445813822663347944758178,
    92575867718337217661963751590579239728245598838407,
    58203565325359399008402633568948830189458628227828,
    80181199384826282014278194139940567587151170094390,
    35398664372827112653829987240784473053190104293586,
    86515506006295864861532075273371959191420517255829,
    71693888707715466499115593487603532921714970056938,
    54370070576826684624621495650076471787294438377604,
    53282654108756828443191190634694037855217779295145,
    36123272525000296071075082563815656710885258350721,
    45876576172410976447339110607218265236877223636045,
    17423706905851860660448207621209813287860733969412,
    81142660418086830619328460811191061556940512689692,
    51934325451728388641918047049293215058642563049483,
    62467221648435076201727918039944693004732956340691,
    15732444386908125794514089057706229429197107928209,
    55037687525678773091862540744969844508330393682126,
    18336384825330154686196124348767681297534375946515,
    80386287592878490201521685554828717201219257766954,
    78182833757993103614740356856449095527097864797581,
    16726320100436897842553539920931837441497806860984,
    48403098129077791799088218795327364475675590848030,
    87086987551392711854517078544161852424320693150332,
    59959406895756536782107074926966537676326235447210,
    69793950679652694742597709739166693763042633987085,
    41052684708299085211399427365734116182760315001271,
    65378607361501080857009149939512557028198746004375,
    35829035317434717326932123578154982629742552737307,
    94953759765105305946966067683156574377167401875275,
    88902802571733229619176668713819931811048770190271,
    25267680276078003013678680992525463401061632866526,
    36270218540497705585629946580636237993140746255962,
    24074486908231174977792365466257246923322810917141,
    91430288197103288597806669760892938638285025333403,
    34413065578016127815921815005561868836468420090470,
    23053081172816430487623791969842487255036638784583,
    11487696932154902810424020138335124462181441773470,
    63783299490636259666498587618221225225512486764533,
    67720186971698544312419572409913959008952310058822,
    95548255300263520781532296796249481641953868218774,
    76085327132285723110424803456124867697064507995236,
    37774242535411291684276865538926205024910326572967,
    23701913275725675285653248258265463092207058596522,
    29798860272258331913126375147341994889534765745501,
    18495701454879288984856827726077713721403798879715,
    38298203783031473527721580348144513491373226651381,
    34829543829199918180278916522431027392251122869539,
    40957953066405232632538044100059654939159879593635,
    29746152185502371307642255121183693803580388584903,
    41698116222072977186158236678424689157993532961922,
    62467957194401269043877107275048102390895523597457,
    23189706772547915061505504953922979530901129967519,
    86188088225875314529584099251203829009407770775672,
    11306739708304724483816533873502340845647058077308,
    82959174767140363198008187129011875491310547126581,
    97623331044818386269515456334926366572897563400500,
    42846280183517070527831839425882145521227251250327,
    55121603546981200581762165212827652751691296897789,
    32238195734329339946437501907836945765883352399886,
    75506164965184775180738168837861091527357929701337,
    62177842752192623401942399639168044983993173312731,
    32924185707147349566916674687634660915035914677504,
    99518671430235219628894890102423325116913619626622,
    73267460800591547471830798392868535206946944540724,
    76841822524674417161514036427982273348055556214818,
    97142617910342598647204516893989422179826088076852,
    87783646182799346313767754307809363333018982642090,
    10848802521674670883215120185883543223812876952786,
    71329612474782464538636993009049310363619763878039,
    62184073572399794223406235393808339651327408011116,
    66627891981488087797941876876144230030984490851411,
    60661826293682836764744779239180335110989069790714,
    85786944089552990653640447425576083659976645795096,
    66024396409905389607120198219976047599490197230297,
    64913982680032973156037120041377903785566085089252,
    16730939319872750275468906903707539413042652315011,
    94809377245048795150954100921645863754710598436791,
    78639167021187492431995700641917969777599028300699,
    15368713711936614952811305876380278410754449733078,
    40789923115535562561142322423255033685442488917353,
    44889911501440648020369068063960672322193204149535,
    41503128880339536053299340368006977710650566631954,
    81234880673210146739058568557934581403627822703280,
    82616570773948327592232845941706525094512325230608,
    22918802058777319719839450180888072429661980811197,
    77158542502016545090413245809786882778948721859617,
    72107838435069186155435662884062257473692284509516,
    20849603980134001723930671666823555245252804609722,
    53503534226472524250874054075591789781264330331690]
    l2 = [int(i) for i in str(sum(l))]

    return l2[0:10]


def largest_collatz_sequence():
    maximum = 0
    longest = 0
    for num in range(2, 1000000):
        n = num
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n/2
            else:
                n = (3*n)+1
        if count > maximum:
            maximum = count
            longest = num

    return longest


def power_digit_sum(power):
    integer = 2**power
    return sum([int(i) for i in str(integer)])

def number_letter_counts(number):
    total = 0
    dictionary = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 10, 200: 10, 300: 12, 400: 11, 500: 11, 600: 10, 700: 12, 800: 12, 900: 11, 1000: 11}
    for n in range(21, number):
        if 20 < n and n < 100:
            units = n % 10
            tens = int(n/10) * 10
            if n % 10 != 0:
                total = dictionary.get(units) + dictionary.get(tens)
                dictionary[n] = total

        elif 100 <= n and n < 1000:
            tens = n % 100
            hundreds = int(n/100)
            if n % 100 != 0:
                total = dictionary.get(tens) + dictionary.get(hundreds) + 10
                dictionary[n] = total


    return sum(dictionary.values())

def counting_sundays(start, end):
    sundays = 0
    d = 2
    days = 0
    nonleap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for year in range(start, end + 1):
        for month in range(1, 13):
            if year % 4 != 0:
                days = nonleap.get(month)
            elif year % 4 == 0 or year == 2000:
                days = leap.get(month)

            calc = days % 7 + d
            d = calc % 7
            print(d)
            if d == 0:
                sundays += 1
    return sundays

def factorial_digit_sum(num):
    factorial = 1
    for n in range(1, num+1):
        factorial *= n

    return sum([int(i) for i in str(factorial)])

def amicable_numbers(number):
    sum3 = 0
    for n in range(1, 10000):
        sum = 0
        sum2 = 0
        for divisors in range(1, n):
            if n % divisors == 0:
                sum += divisors
        for i in range(1, sum):
            if sum % i == 0:
                sum2 += i

        if sum2 == n and sum != n:
            print(n)
            sum3 += n
    return sum3


def names_scores(text):
    count = 0
    total = 0
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
         'Z': 26}

    with open(text, 'r') as f:
        lis = [line.strip() for line in f]
        l = lis[0].split(',')
        l.sort()
        print(l)

    for name in l:
        count += 1
        sum = 0
        for letter in name:
            if letter != '"':
                score = d.get(letter)
                sum += score
        total += (sum * count)

    return total

def non_abundant_sums():
    sum = 0
    l = []
    l1 = []
    for n in range(1, 28124):
        print(n)
        sum = 0
        for divisors in range(1, n):
            if n % divisors == 0:
                sum += divisors

        if sum > n:
            l.append(n)

    print(l)

    for num in range(24, 28124, 2):
        print(num)
        for i in range(0, len(l)-1):
            for j in range(0, len(l)-1):
                if num == l[i] + l[j]:
                    break
                else:
                    if l[j] > num and l[i] > num:
                        l1.append(num)
                        break
    return l1

def thousand_digit_fibonacci_no():
    digits = 0
    f1 = 1
    f2 = 1
    count = 2
    while digits < 1000:
        count += 1
        digits += 1
        fibonacci = f1 + f2
        digits = len(str(fibonacci))
        f1 = f2
        f2 = fibonacci

        return count

import decimal

def reciprocal_cycle(number):
    lis = []
    decimal.getcontext().prec = 100
    for n in range(2, number):
        fraction = str(decimal.Decimal(1 / n))
        print(fraction)
        count = 1
        for l in range(3, len(fraction)-1):
            print(l)
            if fraction[l] != 0:
                if fraction[l] != fraction[2] and fraction[3] != fraction[4]:
                    count += 1
                else:
                    break
        lis.append(count)
    return lis


def self_powers(number):
    sum = 0
    for n in range(1, number+1):
        sum += n**n

    return str(sum)[::-1][0:10][::-1]

def distinct_powers():
    l = []
    for n in range(2, 101):
        for m in range(2, 101):
            l.append(n**m)

    return len(set(l))

def digit_fifth_powers():
    l = []
    total = 0
    for n in range(1, 1000000):
        print(n)
        sum = 0
        number = str(n)
        for d in number:
            sum += int(d)**5
        if sum == n:
            l.append(sum)
    print(l)

    for n in l:
        total += n

    return total

def coin_sums():
    l = [1,2,5,10,20,50,100,200]

def digit_factorials():
    total = 0
    for n in range(1, 1000000):
        number = str(n)
        sum = 0
        for d in number:
            factorial = 1
            for i in range(1, int(d)+1):
                factorial *= i
            sum += factorial

            if sum == n:
                total += n
                print(n)

    return total - 1 - 2

def circular_primes():
    total = 0
    l = ['1','3','7','9']
    for n in range(101, 1000000, 2):
        count = 0
        for i in range(0, len(str(n))):
            if str(n)[i] in l:
                count += 1
        if count == len(str(n)):
            print(n)
            if not any(n % m == 0 for m in range(2, n)):
                count = 0
                num = str(n)
                for rotations in range(1, len(num)):
                    num = num[1: len(num)] + num[0]
                    if not any(int(num) % m == 0 for m in range(2, int(num))):
                        count += 1
                    else:
                        break
                if count == len(str(num)) - 1:
                    total += 1
    return total + 13

def double_base_palindromes():
    sum = 0
    for n in range(1, 1000000):
        string = ''
        if n == int(str(n)[::-1]):
            for i in range(1, 21):
                num = i
                if 2**num > n:
                    break
            integer = n
            for power in reversed(range(0, num)):
                if 2**power > integer:
                    string = string + '0'
                else:
                    string = string + '1'
                    integer -= (2 ** power)
            if string == string[::-1]:
                sum += n

    return sum

def number_spiral_diagonals():
    l = []
    sum = 0
    for n in range(9, 2000000, 2):
        l.append(n)
    start = 0
    for steps in range(2, 501):
        for num in range(start, start + (4*steps), steps):
            sum += l[num]
            print(l[num])
        start = start + (4*steps)

    return sum + 16 + 1002001

def champernowne_constant():
    string = ''
    for n in range(0, 1000000):
        string += str(n)

    product = int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000])
    print(int(string[1]))
    return product

def maximum_paths_sum():
    i = 0
    sum = 0
    l = [[75, 0], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70,98, 73, 93, 38, 53, 60, 4, 23]]
    for n in l:
        print(max(n))
        if n[i] > n[i+1]:
            sum += n[i]
        else:
            sum += n[i+1]
            i = i+1
    return(sum)

def truncatable_primes():
    for n in range(9, 1000):
        count = 0
        state = True
        if not any(n % m == 0 for m in range(2, n)):
            for l in range(0, int(len(str(n)))):
                if str(n)[l] == '1':
                    state = False
            i = n
            num = n
            if state == True:
                for repeats in range(1, len(str(n))+1):
                    if not any(int(i) % m == 0 for m in range(2, int(i))) or not any(num % m == 0 for m in range(2, num)):
                        i = str(i)[1:]
                        num = int(str(n)[:-1])
                        count += 1
                    else:
                        break
            if count == int(len(str(n))-1):
                print(n)

import math
def integer_right_triangles():
    d = {}
    l = []
    for n in range(5, 1000):
        d[n] = 0

    for i in range(3, 1000):
        for j in range(3, 1000):
            hypotenuse = math.sqrt((i**2 + j**2))
            if str(hypotenuse)[-2:] == '.0':
                p = int(hypotenuse + i + j)
                if p < 1000:
                    d[p] += 1
    maximum = max(d.values())
    key = [key for key, val in d.items() if val == maximum]
    return key

def pandigital_prime():
    for n in range(2, 1000000):
        string = ''
        if not any(n % m == 0 for m in range(2, n)):
            ordered = ''.join(sorted(str(n)))
            for i in range(1, len(ordered) + 1):
                string += str(i)
            if string == ordered:
                print(n)


def coded_triangle_number(text):
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
         'Z': 26}
    triangle_nums = []
    count = 0

    for n in range(1, 1000):
        triangle_nums.append(int(n/2 * (n+1)))

    print(triangle_nums)

    with open(text, 'r') as f:
        lis = [line.strip() for line in f]
        l = lis[0].split(',')
    print(l)

    for word in l:
        sum = 0
        for letter in word:
            if letter != '"':
                sum += d.get(letter)
        if sum in triangle_nums:
            count += 1

    return count


def substring_divisibility():
    for n in range(123456789, 9876543211):
        print(n)
        if n >= 123456789 and n <= 999999999:
            n = int('0' + str(n))
        if ''.join(sorted(str(n))) == '0123456789':
            print(n)


def triangular_pentagonal_hexagonal():
    triangular = []
    pentagonal = []
    hexagonal = []
    count = 0

    for n in range(1, 100000):
        print(n)
        triangular.append(int((n * (n+1)) / 2))
        pentagonal.append(int(n*((3*n) - 1) / 2))
        hexagonal.append(int(n * ((2*n) - 1)))

    for i in triangular:
        count += 1
        if i in pentagonal[:count]:
            if i in hexagonal[:count]:
                print(i)


def pentagon_numbers():
    l = []
    for n in range(1, 10000):
        l.append(int(n * ((3*n) - 1)/2))

    print(l)

    for n in range(0, 9999):
        for i in range(n+1, 9999):
            if l[n] + l[i] in l and l[i] - l[n] in l:
                print(l[n], l[i])

def goldbachs_other_conjecture():
    odd = []
    prime = []

    for n in range(2,100):
        if not any(n % m == 0 for m in range(2, n)):
            prime.append(n)

    for n in range(9, 100, 2):
        if any(n % m == 0 for m in range(2, n)):
            odd.append(n)

    print(odd)
    print(prime)

    for num in range(0, len(odd)):
        for n in range(0, len(prime)):
            if odd[num] < prime[n]:
                print(prime[n-1])
                break
            if not (str((odd[num] - prime[n-1]) // 2))[:-1-1] == '.0':
                return num

import math
def goldbachs_other_conjecture2():
    odd = []
    prime = []

    for n in range(2,10000):
        if not any(n % m == 0 for m in range(2, n)):
            prime.append(n)

    for n in range(9, 10000, 2):
        if any(n % m == 0 for m in range(2, n)):
            odd.append(n)

    print(odd)
    print(prime)

    for odd in odd:
        for n in range(1,int(math.sqrt(odd))):
            leftover = odd - (2 * (n ** 2))
            if leftover in prime:
                break
            if n == int(math.sqrt(odd))-1:
                return odd

def permuted_multiples():
    for n in range(1,10000000):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        for digit in str(n):
            l1.append(int(digit))
        l1.sort()
        for digit in str(n*2):
            l2.append(int(digit))
        l2.sort()
        if l1 == l2:
            for digit in str(n*3):
                l3.append(int(digit))
            l3.sort()
            if l1 == l3:
                for digit in str(n*4):
                    l4.append(int(digit))
                l4.sort()
                for digit in str(n*5):
                    l5.append(int(digit))
                l5.sort()
                for digit in str(n*6):
                    l6.append(int(digit))
                l6.sort()

        print(l1)

        if l1 == l2 == l3 == l4 == l5 == l6:
            return n

def combinatoric_selections():
    count = 0
    for n in range(23, 101):
        for r in range(2, 101):
            total1 = 1
            total2 = 1
            total3 = 1
            if n != r:
                for i in range(1, n+1):
                    total1 *= i
                for j in range(1, r+1):
                    total2 *= j
                for k in range(1, ((n+1)-(r+1)+1)):
                    total3 *= k

                if total1 / (total2*total3) > 1000000:
                    count += 1
    return count


def lychrel_numbers():
    count2 = 0
    for n in range(1, 10000):
        count1  = 0
        state = True
        num = n
        while state:
            reverse = str(num)[::-1]
            total = int(reverse) + num
            if str(total) == str(total)[::-1]:
                state = False
            elif count1 < 50:
                count1 += 1
                num = total
            else:
                count2 += 1
                print(n)
                state = False

    return count2

def powerful_digit_sums():
    max = 0
    for a in range(1,100):
        for b in range(1,100):
            sum = 0
            for digits in str(a**b):
                sum += int(digits)
            if sum > max:
                max = sum
    return max

from fractions import Fraction
def square_root_convergents():
    start = 2 + 1/2
    count = 0
    for n in range(1000):
        total = 2 + 1/start
        print(total)
        start = total
        fraction = Fraction(total-1)
        print(fraction)
        for index in range(0, len(fraction)):
            if fraction == '/':
                break
        denominator = fraction[index:]
        numerator = fraction[:index]
        if len(numerator) > len(denominator):
            count += 1

    return count

def spiral_primes():
    num = 3
    spiral = 0
    count = 0
    add = 2
    for step in range(2, 10000, 2):
        spiral += 1
        add += 4
        for n in range(2):
            num += step
            if not any(num % m == 0 for m in range(2, num)):
                count += 1
        num += add
        if not any(num % m == 0 for m in range(2, num)):
            count += 1



        print(count / ((4 * spiral)+1))
        if (count+1) / (4*spiral) < 0.1:
            return (spiral*2)+1



def poker_hands(text):
    l = []
    player_1 = []
    player_2 = []
    player__1 = []
    player__2 = []
    order = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'Q', 'K', 'A']

    with open(text, 'r') as f:
        lis = [line.strip() for line in f]

    for hand in lis:
        l. append(hand.split(' '))
    print(l)

    for hand in l:
        for n in range(0,5):
            player_1.append(hand[:5][n][0])
            player_2.append(hand[5:][n][0])
            player__1. append(hand[:5][n][1])
            player__2.append(hand[5:][n][1])

    start = 0
    end = 5
    for repeats in range(200):
        player1 = 0
        player2 = 0
        count1 = 0
        count2 = 0

        card1 = player__1[0]
        card2 = player__2[0]

        for suit in range(1, 5):
            if card1 == player__1[suit]:
                count1 += 1
            if card2 == player__2[suit]:
                count2 += 1

        if ['T','J','Q','K','A'] in player_1[start: end] and count1 == 4:
            player1 = 10
            break
        elif ['T','J','Q','K','A'] in player_2[start: end] and count2 == 4:
            player2 = 10
            break
        elif count1 == 4:
            player1 = 6
            break
        elif count2 == 4:
            player2 = 6
            break

        start += 5
        end += 5




