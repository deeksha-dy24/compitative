n = int(input())
prices = list(map(int, input().split()))

total = 0

for p in prices:
    print(p, end=" ")
    total += p

print()
print("Total Price =", total)