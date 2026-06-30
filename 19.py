# Find the smallest element

numbers = [12, 45, 8, 67, 23]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)