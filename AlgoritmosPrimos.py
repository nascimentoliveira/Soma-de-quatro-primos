from time import time

#Python 3 script to calculate prime factors of N
def factorization(number):

    #unexpected parameter
    if (number < 2 or type(number) != int):
        print("Expected positive values (natural number, starting at 2)!")
        return 

    factors = list()
    divisor = 2

    while (divisor * divisor <= number):
        if (number % divisor == 0):
            number = int(number/divisor)
            factors.append(str(divisor))
        else:
            if (divisor == 2): divisor += 1
            else: divisor += 2
        
    if (number > 1):
        factors.append(str(number))

    return factors

startTime = time()

number = 1024
result = factorization(number)

if (result != None):
    print("Prime factors of " + str(number) + ":", ", ".join(result))

endTime = time()
print("\n⏱️ Runtime: " + str(endTime - startTime)[:7] + " seconds.")

#Python 3 script that determines the primality of a number
def isPrime(number):

    #unexpected parameter
    if (number < 2 or type(number) != int):
        print("Expected positive values (natural number, starting at 2)!")
        return

    if (len(factorization(number)) == 1):
        return True
    else:
        return False
      
startTime = time()

number = 97
result = isPrime(number)
if (result != None):
    print("The number " + str(number) + " is", 'prime.' if isPrime(number) else 'not prime.')

endTime = time()
print("\n⏱️ Runtime: " + str(endTime - startTime)[:7] + " seconds.")

#Python 3 script to find two primes that add up to N, for N even
def goldbach(number):
    
    #unexpected parameter
    if (number < 4 or type(number) != int):
        print("Expected positive values (natural number, starting at 4)!")
        return
    
    portion = 2

    while (portion <= number):
        if (isPrime(portion) and isPrime(number - portion)):
            return portion, number - portion 
   
        if (portion == 2): portion += 1
        else: portion += 2
          
        
startTime = time()

number = 14
result = goldbach(number)
if (result != None):
    print("The number " + str(number) + " is the result of the sum (of the primes) " + str(result[0]) + " + " + str(result[1]) + '.')

endTime = time()
print("\n⏱️ Runtime: " + str(endTime - startTime)[:7] + " seconds.")

def fork(number):
    if (number % 2 == 0):
        return int(number/2), int(number/2)
    else:
        return int(number/2 - 0.5), int(number/2 + 0.5)
      
#Python 3 script to find 4 prime parcels that add up to a number
def fourPrimes(number):

    if (number < 8 or type(number) != int):
        print("Expected positive values (natural number, starting at 8)!")
        return
    
    parcelTemp1, parcelTemp2 = fork(number)

    parity = (parcelTemp1 % 2) + (parcelTemp2 % 2)

    if (parity == 0):
        prime1, prime2 = goldbach(parcelTemp1)
        prime3, prime4 = goldbach(parcelTemp2)
    
    elif (parity == 2):
        parcelTemp1 += 1
        parcelTemp2 -= 1
        prime1, prime2 = goldbach(parcelTemp1)
        prime3, prime4 = goldbach(parcelTemp2)
    
    else:
        if (parcelTemp1 % 2 == 0):
            evenParcel = parcelTemp1
            oddParcel = parcelTemp2
        else:
            evenParcel = parcelTemp2
            oddParcel = parcelTemp1
    
        while not (isPrime(oddParcel - 2)):
            evenParcel += 2
            oddParcel -= 2
            
        prime1 = 2
        prime2 = oddParcel - prime1
        prime3, prime4 = goldbach(evenParcel)
            
    return [str(prime1), str(prime2), str(prime3), str(prime4)]
  
startTime = time()

number = 5252694
result = fourPrimes(number)
if (result != None):
    print("The number " + str(number) + " is the result of the sum (of the primes)" , " + ".join(result))

endTime = time()
print("\n⏱️ Runtime: " + str(endTime - startTime)[:7] + " seconds.")
