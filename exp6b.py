n = int(input().strip())
packets = list(map(int, input().strip().split()))

# Ensure correct number of packets
if len(packets) != n:
    print("ANOMALY")
else:
    checksum = int(input().strip())

    xor_value = 0
    for packet in packets:
        xor_value ^= packet

    if xor_value == checksum:
        print("OK")
    else:
        print("ANOMALY")