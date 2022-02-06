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


def q5():
  
print("Problem 1 answer: ", q1(1000))
print("Problem 2 answer: ", q2(4000000))
print("Problem 3 answer: ", q3(600851475143))
print("Problem 4 answer: ", q4())
print("Problem 5 answer: ", q5())