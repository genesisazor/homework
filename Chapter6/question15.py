def is_odd(n):
    if is_even(n):
        return False
    else:
        return True


test(is_odd(2) == False)
test(is_odd(1) == True)
