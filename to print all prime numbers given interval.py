start = 11
end = 75
print("prime number between", start, "and", end, "are:")

for i in range(start, end + 1):
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        
        # This IF stays outside the 'j' loop so it only prints ONCE per number
        if is_prime == True:
            print(i, end=",")
