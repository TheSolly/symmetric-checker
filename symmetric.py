# A procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on.


def symmetric(x):
    for row in x:
        if len(row) != len(x):
            return False
    y = []
    for p in range(len(x)):
        y.append([q[p] for q in x])
    if x == y:
        return True
    return False


print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]])
# >>> False

print symmetric([[1, 2],
                 [2, 1]])
# >>> True

print symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]])
# >>> False

print symmetric([[1, 2, 3],
                 [2, 3, 1]])
# >>> False
