n = int(input())
lengths = list(map(int, input().split()))
speeds = list(map(int, input().split()))

left = 0
right = n - 1
max_time = 0

while left <= right:
    # Avoid division by zero
    if speeds[left] != 0:
        time_left = lengths[left] / speeds[left]
        max_time = max(max_time, time_left)

    if left != right and speeds[right] != 0:
        time_right = lengths[right] / speeds[right]
        max_time = max(max_time, time_right)

    left += 1
    right -= 1

print(int(max_time))