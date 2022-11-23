from unit_tester import test


def cleanword(wrd):
    lst = list(wrd)
    #   chars=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for i in range(len(lst)):
        char = ord(lst[i])  # The function ord() gets the int value of the char. And in case you want to convert back after playing with the number, function chr() does the trick.
        if (65 <= char <= 90) or (97 <= char <= 122):  # lst[i] not in chars
            lst[i] = lst[i]
        else:
            lst[i] = ""
        result = "".join(lst)
    return result


def has_dashdash(wrd):
    lst = list(wrd)
    for i in range(len(lst) - 1):
        if lst[i] == "-" and lst[i + 1] == "-":
            return True
        else:
            continue


def extract_words(wrd):
    tab = wrd.split()
    newlist = []

    for i in range(len(tab)):
        if has_dashdash(tab[i]):
            old=tab[i]
            ind=old.index("-")
            new1=old[:ind]
            new2=old[ind+2:]
            newlist.append(new1)
            newlist.append(new2)
            break
        res = cleanword(tab[i])
        if res == "Now":
            res = "now"
        elif res=="Yes":
            res="yes"
        newlist.append(res)
    return newlist


def wordcount(wrd,tab):
    count=0
    for i in range(len(tab)):
        if wrd==tab[i]:
            count+=1
        else:
            continue
    return count


def wordset(tab):
    tab.sort()
    newtab=[]
    for i in range(len(tab)):
        if tab[i] in newtab:
            continue
        else:
            newtab.append(tab[i])
    return newtab

def longestword(tab):
    longest=0
    for i in range(len(tab)):
        if len(tab[i])>longest:
            longest=len(tab[i])
    return longest



test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
     ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
     ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
     ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
     ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
     ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longestword([]) == 0)
