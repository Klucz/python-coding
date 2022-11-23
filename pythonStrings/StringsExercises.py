import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def find(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def char(strng, i):
    return (strng[i])


# if "Python"[1]=="y":
#    print("Python[1] ok")
print("Python"[1])
print("Strings are sequences of characters."[5])
print("Length of wonderful is: ", len("wonderful"))
print("Mystery"[:4])
print("p" in "Pineapple")
print("apple" in "Pineapple")
print("pear" not in "Pineapple")
print("apple" > "pineapple")
print("pineapple" < "Peach")

test(char("Python", 1) == "y")
test(char("Strings are sequences of characters.", 5) == "g")
# test(mysum([1, -2, 3]) == 2)
# test(mysum([ ]) == 0)
# test(mysum(range(11)) == 55)  # 11 is not included in the list.

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O":
        letter = "Ou"
    if letter == "Q":
        letter = "Qu"
    print(letter + suffix)


# def count_letters(string,ltr):
#    count = 0
#    for i in string:
#        if i == ltr:
#            count += 1
#    return count

def count_letters(string, ltr):
    count = 0
    for i in range(len(string)):  # Loop not to count same letter twice or more
        a = (string.find(ltr, i))
        b = (string.find(ltr, i + 1))
        if a != b:
            print("Letter position is: ", string.find(ltr, i))
        else:
            continue  # If letter position is the same start counting from new position
        if (string.find(ltr, i)) != -1:
            count += 1
    return count


print("Number of letters: ", count_letters("banana", "n"))


def reverse(strng):
    i = 0
    rev = ""
    while i < len(strng):
        newchar = strng[abs(len(strng) - 1 - i)]
        rev += newchar
        i += 1
    return rev


test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")


def mirror(strng):
    rev = reverse(strng)
    newstring = strng + rev
    return newstring


test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")


def remove_letter(ch, strng):
    i = 0
    newstring = ""
    while i < len(strng):
        if strng[i] == ch:
            newstring += ""
            i += 1
        else:
            newstring += strng[i]
            i += 1
    return newstring


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")


def is_palindrome(strng):
    rev = reverse(strng)
    if strng == rev:
        return True


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))  # Is an empty string a palindrome?


def count(subs, strng):
    i = 0
    count = 0
    while i < len(strng):
        a = strng.find(subs, i)
        if a == -1:
            break
        count += 1
        i = a + 1
    return count


test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)


def remove(subs, strng):
    i = 0
    newstring = ""
    while i < len(strng):
        a = strng.find(subs, i)
        if a == -1:
            return strng
        newstring = strng[0:a] + strng[a + len(subs):]
        return newstring


test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")


def remove_all(subs, strng):
    i = 0
    newstring = ""
    a = strng.find(subs, i)
    if a == -1:
        return strng
    while i < len(strng):
        a = strng.find(subs, 0)
        if a == -1:
            break
        newstring = strng[0:a] + strng[a + len(subs):]
        strng=newstring

    return newstring


test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")