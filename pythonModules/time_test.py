import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000        # Lets have 10 million elements in the list
testdata = range(sz)

t0 = time.monotonic()
my_result = do_my_sum(testdata)
t1 = time.monotonic()
print("my_result    = {0} (time taken = {1:.4f} seconds)"  # my_result    = 49999995000000 (time taken = 0.3280 seconds)
        .format(my_result, t1-t0))

t2 = time.monotonic()
their_result = sum(testdata)
t3 = time.monotonic()
print("their_result = {0} (time taken = {1:.4f} seconds)"  # their_result = 49999995000000 (time taken = 0.2970 seconds)
        .format(their_result, t3-t2))