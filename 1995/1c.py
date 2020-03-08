print("Patrick Connolly - Eton College")

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