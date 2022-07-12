########################
#   Prints the largest number from a few given numbers
########################

def largest(a, *args):
    large = a
    for b in args:
        if b > large:
            large = b
    return large

print(largest(5, 6, 69, 27, 15, 22))