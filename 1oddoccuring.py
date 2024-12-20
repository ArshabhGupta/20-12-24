def oddOccuring(arr):
    result = 0
    for element in arr:
        result = result ^ element
    return result

arr = []
n = int(input("Enter your array size: "))
while (n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n -= 1
print(oddOccuring(arr))