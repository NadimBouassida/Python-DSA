"""
867. Transpose Matrix
"""
def transpose(matrix):
    
    rows_count = len(matrix)
    column_length = len(matrix[0])
    
    result = [[matrix[i][j] for i in range(rows_count)] for j in range(column_length)] 
    
    return result


test_cases = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]]]
for test in test_cases:
    print(transpose(test))
        
        