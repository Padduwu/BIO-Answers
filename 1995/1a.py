import math

input = int(input("Enter a number: "))
def pallindrome(num):
    for i in range(num+1,10**20):
        if i == int(str(i)[::-1]):
            print(i)
            return i

pallindrome(input)

