import sys


def turn_clockwise(a):
    if a == "N":
        return "E"
    elif a == "E":
        return "S"
    elif a == "S":
        return "W"
    elif a == "W":
        return "N"


def day_name(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"


def day_num(num):
    if num == "Sunday":
        return 0
    elif num == "Monday":
        return 1
    elif num == "Tuesday":
        return 2
    elif num == "Wednesday":
        return 3
    elif num == "Thursday":
        return 4
    elif num == "Friday":
        return 5
    elif num == "Saturday":
        return 6


def day_add(dayname, number):
    n = day_num(dayname)
    delta = (n + number) % 7
    if (n + delta) > 7:
        delta = (n + delta) % 7
        return day_name(delta)
    else:
        return day_name(delta)


def days_in_month(month):
    if month == "February":
        return 28
    elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        return 31
    elif month == "April" or month == "June" or month == "September" or month == "November":
        return 30


def to_secs(h, m, s):
    return int(h * 3600 + m * 60 + s)


def hours_in(sc):
    return int(sc / 3600)


def minutes_in(sc):
    sc = sc % 3600
    return int(sc / 60)


def seconds_in(sc):
    sc = sc % 3600
    sc = sc % 60
    return sc


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def hypotenuse(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def slope(x1, y1, x2, y2):
    return float(y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    sl = slope(x1, y1, x2, y2)
    con = y1 - x1 * sl
    return con


def is_even(n):
    n = int(n)
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    n = int(n)
    b = is_even(n)
    if b == True:
        return False
    else:
        return True


def is_factor(f, n):
    int(f)
    int(n)
    res = (n/f)
    if res-int(res) != 0:
        return False
    else:
        return True


def is_multiple(f, n):
    int(f)
    int(n)
    res = (f / n)
    if res - int(res) != 0:
        return False
    else:
        return True


def f2c(f):
    c=(f-32)*5/9
    return round(c)


def c2f(c):
    f = c*9/5+32
    return round(f)




def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("S") == "N")
    test(turn_clockwise("N") == "S")
    test(turn_clockwise("S") == "W")
    test(turn_clockwise("E") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)


test_suite()  # Here is the call to run the tests


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)


test_suite()  # Here is the call to run the tests


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)


test_suite()  # Here is the call to run the tests


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """


test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
test_suite()  # Here is the call to run the tests


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """


test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
test(days_in_month("rubbish") == None)

test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)

test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433, 0, 0) == 8758)

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)

test_suite()  # Here is the call to run the tests

test(3 % 4 == 0)
test(3 % 4 == 3)
test(3 / 4 == 0)
test(3 // 4 == 0)
test(3 + 4 * 2 == 14)
test(4 - 2 + 2 == 0)
test(len("hello, world!") == 13)

test(compare(5, 4) == 1)
test(compare(7, 7) == 0)
test(compare(2, 3) == -1)
test(compare(42, 1) == 1)

test(hypotenuse(3, 4) == 5.0)
test(hypotenuse(12, 5) == 13.0)
test(hypotenuse(24, 7) == 25.0)
test(hypotenuse(9, 12) == 15.0)

test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)

test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)

test(is_even(2))
test(is_even(1))
test(is_even(10))

test(is_odd(2))
test(is_odd(1))
test(is_odd(10))

test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))

test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))


test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)

test(c2f(0) == 32)
test(c2f(100) == 212)
test(c2f(-40) == -40)
test(c2f(12) == 54)
test(c2f(18) == 64)
test(c2f(-48) == -54)