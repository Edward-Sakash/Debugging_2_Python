def fizzbuzz(maximum_value):
    for n in range(maximum_value):
        if n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz')
        else:
            print(n)
print(fizzbuzz(315))            

##################################################

"""import ipdb

def fizzbuzz(maximum_value):
    ipdb.set_trace()  # Set breakpoint here
    for n in range(maximum_value):
        if n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz')
        else:
            print(n)

fizzbuzz(15)"""

print("_______________________________________________")

