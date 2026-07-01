# Move all zeros to the end

numbers = [1, 0, 2, 0, 3, 0, 4, 5]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

while len(result) < len(numbers):
    result.append(0)

print("After moving zeros:", result)