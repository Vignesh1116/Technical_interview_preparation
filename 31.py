# Bubble Sort

numbers = [5, 3, 8, 1, 2]

for i in range(len(numbers)): # 01234
    for j in range(len(numbers) - 1): # 0123
        if numbers[j] > numbers[j + 1]: # 5>3 3>8 8>1 
            temp = numbers[j] # 5 3
            numbers[j] = numbers[j + 1] # 3 8
            numbers[j + 1] = temp # 5 1
#35812
print("Sorted array:", numbers)