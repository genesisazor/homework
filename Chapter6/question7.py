
n=25
approx = n/2
while True:
    better = (approx + n/approx)/2
    if abs(better-approx) <.0000001:
        if better ** 2 == n:
            print("accurate")
        else:
              print("approximate")
       break
    approx = better
    print(better)
print(better)

