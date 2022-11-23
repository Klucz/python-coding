this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))  # a and b have the same value but do not refer to the same object.
# Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object.
# This is not the case with lists:
