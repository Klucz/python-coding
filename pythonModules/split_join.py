from unit_tester import test

s = "If we took the bones out, it wouldn't be crunchy, would it?"
s.split()
type(s.split())
s.split("o")
s.split("i")
"0".join(s.split("o"))


def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    s2=s.split()
    tab = list(" ".join(s2))
    for i in range(len(tab)):
        if tab[i] == old:
            tab[i] = new
        result = "".join(tab)
    return result


test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")