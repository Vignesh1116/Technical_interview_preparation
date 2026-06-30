# Find the largest element

numbers = [10, 25, 7, 40, 18]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)