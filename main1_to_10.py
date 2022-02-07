import math

def q1(n):
  #Find the sum of all multiples of 3 and 5 up to n
  sumn = 0
  for i in range(1, n):
    if i % 3 == 0:
      sumn += i
    elif i % 5 == 0:
      sumn += i
    else:
      pass
  return sumn


def fiblimit(n):
  flist = [1, 1]
  while flist[-1] < n:
    flist.append(flist[-1] + flist[-2])
  return flist



def q2(n):
  # Find the sum of the even Fibbonacci numbers up to n
  rsum = 0
  for i in fiblimit(n):
    if i % 2 == 0:
      rsum += i

  return rsum
def product(n):
  rproduct = 1
  for i in n: 
    rproduct *= i
  return rproduct

def q3(n):
  #Find the largest prime factor of n
  norig = n
  nsqrt = n ** 0.5
  plist = []
  while product(plist) != norig:
    nsqrt = int(n ** 0.5)
    if nsqrt < 2:
      return max(plist)
    for i in range(2, int(nsqrt)):
      if n % i == 0:
        plist.append(int(i))
        n = n/i
  return max(plist)



def isPalindrome(n):
  nstr = str(n)
  return nstr == nstr[::-1]


def q4():
  #Largest palindrome from the product of two three-digt numbers
  palindromes = []
  for i in range(100, 999):
    for j in range(100, 999):
      p = i * j
      if isPalindrome(p):
        palindromes.append(p)
  return max(palindromes)

def gcf(a, b):
  #Euclid's method
  r=a%b
  while r:
      a=b
      b=r
      r=a%b
  return b

def lcm(a, b):
  # ab / gcf(a, b)
  return int((a * b) / gcf(a, b)) 

def q5():
  #Least common multiple of numbers 1 through 20
  rlist = list(range(1, 20))
  templcm = 1
  for i in rlist: 
    templcm = lcm(i, templcm)
  return templcm

def q6(n):
  #Difference between square of sum of natural numbers and sum of natural number squared
  nlist = list(range(1, n))
  squarelistsum = sum([i ** 2 for i in nlist])
  squaredsum = sum(nlist) ** 2
  return squaredsum - squarelistsum


def q7(n):
  #a little cheat https://codereview.stackexchange.com/questions/102507/finding-the-10001st-prime
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]


def q8():
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    #find the thirteen adjacent digits in a thousand-digit number that have the highest product
    nstr = str(n)
    highestProduct = 0
    chunks = [[int(j) for j in nstr[i:i + 13]] for i in range(0, len(nstr) - 13)]
    for chunk in chunks:
        if highestProduct < product(chunk):
            highestProduct = product(chunk)
    return highestProduct   


def q9():
    #find a pythagorean triple where a + b + c sum to 1000
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a ** 2 + b ** 2)
            if (int(c) - c == 0.0) and (a + b + c == 1000) and (a < b) and (b < c):
                return a * b * c

def q10(end):
    #I am italics(really) bad with primes https://codereview.stackexchange.com/questions/126347/project-euler-problem-10
    is_prime = [i not in [0, 1] for i in range(end+1)]

    for prime in range(end+1):
        if not is_prime[prime]:
            continue
        if prime * prime > (end + 1):
            break
        for multiple_of_prime in range(2*prime, end+1, prime):
            is_prime[multiple_of_prime] = False

    return sum(num for num in range(end+1) if is_prime[num])


print("Problem 1 answer: ", q1(1000))
print("Problem 2 answer: ", q2(4000000))
print("Problem 3 answer: ", q3(600851475143))
print("Problem 4 answer: ", q4())
print("Problem 5 answer: ", q5())
print("Problem 6 answer: ", q6(100))
print("Problem 7 works but takes too long to calc(invloving primes.) Moving on to problem 8...")
#print("Problem 7 answer: ", q7(10001))
print("Problem 8 answer: ", q8())
print("Problem 9 answer: ", q9())
print("Problem 10 answer: ", q10(2000000))

