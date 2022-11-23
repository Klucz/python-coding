import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

count = 0
sum = 0
for f in [13, 12, 10, 8, 66, 45, 77, 88]:
    if f % 2 == 1:
        count += 1
print(count)

for f in [13, 12, 10, 8, 66, 45, 77, 88]:
    if f % 2 == 0:
        sum += f
print(sum)

sum = 0
for f in [-13, 12, 10, 8, -66, 45, -77, 88]:
    if f < 0:
        sum += f
print(sum)

count = 0
for f in ["krzeslo", "wanna", "stolik"]:
    if len(f) == 5:
        count += 1
print(count)

tab = [-13, 13, 13, 7, -77, 45, -77, 99]


def suma_do_pierwszej_parzystej(tab_wew):
    sum_wew = 0
    for f in tab_wew:
        if f % 2 == 0:
            break
        else:
            sum_wew += f

    return sum_wew
    print(sum_wew)


suma_do_pierwszej_parzystej(tab)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(suma_do_pierwszej_parzystej([-13,12]) == -13)
    test(suma_do_pierwszej_parzystej([55,33,44,22]) == 88)
    test(suma_do_pierwszej_parzystej([13,15,17]) == 45)

test_suite()        # Here is the call to run the tests


def words_count(tab_wew):
    count = 0
    for f in tab_wew:
        if f == "sam":
            count += 1
            break
        else:
            count += 1

    return count
    print(count)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(words_count(["dupa","sam"]) == 2)
    test(words_count(["aaaa","bbbbb","cccccc","dddddddd"]) == 4)
    test(words_count(["asdasd","sadasdasd","asdasdasdas","fh302h98r23fh","sam"]) == 5)

test_suite()        # Here is the call to run the tests
