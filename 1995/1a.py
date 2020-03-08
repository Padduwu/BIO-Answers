print("Patrick Connolly - Eton College")

input = int(input("Enter a number: "))

def palindrome(num):
    for i in range(num+1,10**20):
        if str(i) == str(i)[::-1]:
            print(i)
            return i

palindrome(input)

