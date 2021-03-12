num_cases = int(input())
for _ in range(num_cases):
    array_size, num_rotations = map(int, input().strip().split())
    num_rotations = num_rotations%array_size
    
    array = list(map(int, input().strip().split()))

    threshold = len(array) - num_rotations
    new_array = []
    for i in range(threshold, len(array)):
        new_array.append(array[i])
    for i in range(0, threshold):
        new_array.append(array[i])
    
    for item in new_array:
        print(item, end=' ')
    print()
