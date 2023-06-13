#Find the n'th number in the fibonacci sequence
# The Fibonacci sequence is defined as follows. The first number of the sequence
# is 0, the second number of the sequence is 1 and the following
#  numbers in the sequence (n) are the sum of the previous 2 numbers
#  before it.

# The following function is provided as starter code for exploring

# Print out the values being memoized in a set
# This function returns values quite fast O(n) time or O(n) space,
#  it also has an error

#  Solution

fib_dict = {1: 0, 2: 1}  # Initial dictionary with the first two Fibonacci numbers

def get_n(n, memoize=None):
    if memoize is None:
        memoize = fib_dict  # Use the predefined dictionary if memoize is None

    if n in memoize:  # If the value is already memoized, return it
        return memoize[n]
    else:
        # Calculate the Fibonacci number recursively by summing the previous two numbers
        memoize[n] = get_n(n - 1, memoize) + get_n(n - 2, memoize)
    
    return memoize[n]  # Return the calculated Fibonacci number

print(get_n(78, fib_dict))  # Calculate and print the 10th Fibonacci number




# Solution
def get_n(n, memoize=None):
    if memoize is None:
        memoize = {1: 0, 2: 1}

    print("Memoizing:", memoize.keys())

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_n(n - 1, memoize) + get_n(n - 2, memoize)
        return memoize[n]

# Prompt the user for input
n = int(input("Enter the value of n: "))

result = get_n(n)
print(f"The {n}th number in the Fibonacci sequence is: {result}")

print("______________________________________________")

def get_n(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_n(n - 1, memoize) + get_n(n - 2, memoize)
    return memoize[n]
print(get_n(78))