def fib(n):
    results = []
    a, b = 0, 1
    while a < n:
        results.append(a)
        a, b = b, a+b
    return results


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("integer changed to zero.")
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("More")

results = fib(x)
print(results)

words = ['car', 'window', 'somedword']

for w in words:
    print(w, len(w))

for i in range(5, 9):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for r in range(len(a)):
    print(r, a[r])