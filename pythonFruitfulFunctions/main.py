def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
           return wd
    return ""


find_first_2_letter_word(["This",  "is", "a", "dead", "parrot"])
find_first_2_letter_word(["I",  "like",  "cheese"])