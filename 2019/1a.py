print("Patrick Connolly - Eton College - Age 16\n")
print("British Informatics Olympiad 2019 - Question 1a\n")

num = int(input("Enter a number: "))

for i in range(num+1,10**20):
    if str(i) == str(i)[::-1]:
        print(i)
        break
        



