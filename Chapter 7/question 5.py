def test_suite():
    """Run the suite of tests for code in this module (this file)."""

    print("tests for 5 words")
    test(words_5(names) == 4)
    test(sum_to_even(xs)==-2)

xs=[1,-3,2,4,14,23,34,42,-57]

def sum_to_even(nlist):
    """Sum all the elements in a list of up to but not including the first even number."""

    sum = 0
    for i in nlist:
        if i % 2 == 0:
            break
        else:
            sim+=i
    return sum