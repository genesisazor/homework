xs[1,-3,2,4,14,23,34,42,-57]
def neg_sum(nlist):
    """sum of all negative nums in list"""
    total = 0
    for i in nlist:
        if i < 0:
            total+=i
    return total
print(neg_sum(xs))
