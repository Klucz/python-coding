import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def is_prime(arg):
    if arg == 1:
        return False
    if arg == 2 or arg == 3 or arg == 5 or arg == 7:
        return True
    if arg % 2 != 0 and arg % 3 != 0 and arg % 5 != 0 and arg % 7 != 0:
        return True
    else:
        return False


def test_suite():
    # For your test suite
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(89))


test_suite()
