print("Patrick Connolly - Eton College - Age 16\n")
print("British Informatics Olympiad 2019 - Question 1c\n")
print("How many integers are there, between 1 and 99999 inclusive, that are not the sum of two palindromic numbers?\n")

palindromes = [False for _ in range(99999)]
numbers = [False for _ in range(99999)]

for i in range(0,99999):
    if str(i) == str(i)[::-1]:
        palindromes[i] = True


for i in range(0, 99999):
	if palindromes[i] == True:
		for j in range(i, 99999):
			if palindromes[j] == True:
				if i+j < 99999:
					numbers[i+j] = True

print(numbers.count(False))

#Answer: 9030