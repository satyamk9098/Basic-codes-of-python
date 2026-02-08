def set_sum(arr):
    total = 0
    for i in arr:
        total = total + i
    return total

arr = [12, 3, 4, 15]
n = len(arr)
ans = set_sum(arr)
print("sum of the array is:", ans)
