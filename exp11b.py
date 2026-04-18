n = int(input())
prices = list(map(int, input().split()))
qty = list(map(int, input().split()))

total = 0

for i in range(n):
    total += prices[i] * qty[i]

print(total)