# Linear Search

numbers = [10, 20, 30, 40, 50]

key = 30

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at index", i)
        break
else:
    print("Element not found")