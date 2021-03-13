num_cases = int(input())
for _ in range(num_cases):
    array_size = int(input())
    array = list(map(int, input().strip().split()))
    array.sort() #O(nlogn)
    min_output = float('inf')
    for i in range(array_size-1): # O(n) - minimum of XOR can only be present between sorted pair of values in an array.
        a = array[i]
        b = array[i+1]
        output = a^b #((a AND b)XOR(a OR b)) can be simplified to (a XOR b)
        if(min_output>output):
            min_output = output
    print(min_output)
