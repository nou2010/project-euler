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

#print("Problem 1 answer: ", q1(1000))
#print("Problem 2 answer: ", q2(4000000))
#print("Problem 3 answer: ", q3(600851475143))
#print("Problem 4 answer: ", q4())
#print("Problem 5 answer: ", q5())
#print("Problem 6 answer: ", q6(100))
print("Problem 7 answer: ", q7(10001))