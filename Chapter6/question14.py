def is_even(n):
    if n % 2 == 1:
        return False
    elif n % 2 == 0:
        return True


test(is_even(8) == True)
test(is_even(-7) == False)
