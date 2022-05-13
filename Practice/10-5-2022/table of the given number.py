x=int(input("Enter a Number:")) #Table of the given number
def table(x):
    for i in range(1,5):
        print(x, "x", i, "=", x * i)
table(x)