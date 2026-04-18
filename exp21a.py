from collections import defaultdict

n = int(input())
tree = defaultdict(list)
file_index = set()   # ✅ better than dict for search

for _ in range(n):
    directory, file = input().split()
    tree[directory].append(file)
    file_index.add(file)

search_file = input()

print("File System Structure")
for directory in tree:
    print(directory, "->", *tree[directory])

print("\nSearch Result")
if search_file in file_index:
    print("File Found")
else:
    print("File Not Found")