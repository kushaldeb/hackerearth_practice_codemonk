num_cases = int(input())
for _ in range(num_cases):
    matrix_order = int(input())
    matrix = []
    matrix_array = []
    
    for order in range(matrix_order):
        matrix_array = list(map(int, input().strip().split()))
        matrix.append(matrix_array)
    
    num_inversions = 0
    for i in range(0, matrix_order):
        for j in range(0, matrix_order):
            key = matrix[i][j]
            for p in range(i, matrix_order):
                for q in range(j, matrix_order):
                    if(key>matrix[p][q]):
                        num_inversions += 1
    print(num_inversions)
