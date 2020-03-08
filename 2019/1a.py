print("Patrick Connolly - Eton College - Age 16\n")
print("British Informatics Olympiad 2019 - Question 1a\n")
print("Write a program that reads in a positive integer of up to 20 digits.")
print("You should output the smallest palindromic number that is higher than the input.\n")

num = int(input("Enter a number: "))

for i in range(num+1,10**20):
    if str(i) == str(i)[::-1]:
        print(i)
        break
        



