# Find kth largest element

numbers = [10, 50, 30, 20, 40]

k = 3 

numbers.sort(reverse=True) # 50 40 30 20 10

print(k, "largest element is:", numbers[k - 1])