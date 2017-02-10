
#print 1-100 numbers in sequence
i = list(range(101))
print ("sequence numbers:", i)

#print even numbers between 1 - 100
evens = [i for i in range(101) if i % 2 == 0]
print ("list of even numbers: ",evens)

#print odd numbers between 1 - 100
odds = [i for i in range (101) if i % 2!= 0]
print ("list of odd numbers: ", odds)

#print prime numbers between 1 - 100
primes = [i for i in range(2, 101) if i not in evens]
print ("list of prime numbers: ", primes)
