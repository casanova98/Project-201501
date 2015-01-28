
answer = input("Enter your whole number here to find its factors!!!!")

n = int(answer)

factors = []
for i in range(1, n):
    if n % i == 0:
        factors.append(i)
print("The factors are in the following set", factors)






