def checkIfSame(n1, n2):
    if (n1 ^ n2) != 0:
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
checkIfSame(n1, n2)