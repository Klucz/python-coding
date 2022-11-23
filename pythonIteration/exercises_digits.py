import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def num_digits(n):
    n = abs(n)
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count = count + 1
        n = n // 10
    return count


test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
test(num_digits(-24) == 2)


def num_even_digits(n):
    n = abs(n)
    count = 0
    if n == 0:
        return 1
    while n != 0:
        if n % 2 == 0:
            count = count + 1
        n = n // 10
    return count


test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)


def sum_of_squares(xs):
    suma = 0
    for i in xs:
        suma += i**2
    return suma


test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)