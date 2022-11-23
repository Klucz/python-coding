import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

# Add tests like these to your test suite ...
test(mysum([1, 2, 3, 4]) == 10)
test(mysum([1.25, 2.5, 1.75]) == 5.5)
test(mysum([1, -2, 3]) == 2)
test(mysum([ ]) == 0)
test(mysum(range(11)) == 55)  # 11 is not included in the list.


def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss


def test_suite():

    # For your test suite
    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)


test_suite()


def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")


seq3np1(3)
#3, 10, 5, 16, 8, 4, 2, 1.
seq3np1(19)
#19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13,
#                    40, 20, 10, 5, 16, 8, 4, 2, 1.
seq3np1(21)
#21, 64, 32, 16, 8, 4, 2, 1.
seq3np1(16)
#16, 8, 4, 2, 1.


def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(710))

def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count


test(num_zero_and_five_digits(1055030250) == 7)
test(num_digits(0) == 1)


for x in range(13):   # Generate numbers 0 to 12
    print(x, "\t", 2**x)


for i in range(1, 7):
    print(2 * i, end="   ")
print()


def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()


for i in range(1, 7):
    print_multiples(i)