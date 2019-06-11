a = int(input())
b = int(input())
s = 0
for num in range((b + 1), a):
    if (num % 2):
        s += num
print(s)