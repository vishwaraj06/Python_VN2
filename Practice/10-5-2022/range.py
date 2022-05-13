def test_range(n):
    if n in range(2,49):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
n=int(input("Enter number to check:"))
test_range(n)