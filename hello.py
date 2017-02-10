def main():
    Choices = dict(
        one = 'First',
        two = 'Second',
        three = 'Third',
        four = 'Fourth',
        five = 'Fifth'
    )
    v = 'seven'
    print(Choices.get(v, 'other'))
if __name__ == "__main__": main()


def main():
    a, b = 0, 1
    v = "this is true" if a>b else "this is not true"
    print (v)

if __name__ == "__main__": main()


def main():
    counter = 100          # An integer assignment
    miles = 1000.0       # A floating point
    name = "John"       # A string

    print(counter)
    print(miles)
    print(name)

if __name__ == "__main__": main()


def main():
    tuple = ('abcd', 786 , 2.23, 'john', 70.2)
    tinytuple = (123, 'john')

    print(tuple)           # Prints complete list
    print(tuple[0])        # Prints first element of the list
    print(tuple[1:3])      # Prints elements starting from 2nd till 3rd
    print(tuple[2:])       # Prints elements starting from 3rd element
    print(tinytuple * 2)   # Prints list two times
    print(tuple + tinytuple) # Prints concatenated lists

if __name__ == "__main__": main()



def main():
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
    #list = ['abcd', 786 , 2.23, 'john', 70.2 ]
    #print (list)
    #tuple[2] = 1000    # Invalid syntax with tuple
    #list[2] = 1000    # Valid syntax with list
    #print(list)
    print(tuple)

if __name__ == "__main__": main()



def main():
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


    print(dict['one'])       # Prints value for 'one' key
    print(dict[2])           # Prints value for 2 key
    print(tinydict)          # Prints complete dictionary
    print(tinydict.keys())   # Prints all the keys
    print(tinydict.values()) # Prints all the values

if __name__ == "__main__": main()





x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y and x > z:
    maximum = x
elif y > x and y > z:
    maximum = y
else:
    maximum = z

print("The maximal value is: " + str(maximum))



n = 3

s = 0
counter = 1
while counter <= n:
    s = s + counter
    counter += 1

print("Sum of 1 until %d: %d" % (n,s))



edibles = ["ham","spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

print("xyz)
print("good job krthink")
