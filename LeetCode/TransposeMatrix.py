"""
867. Transpose Matrix
"""
def transpose(matrix):

    # Without List Comprehension:
    # r = len(matrix) # Number of rows in the Matrix
    # c = len(matrix[0]) # Length of each column in the Matrix
    # transpose = [[0 for i in range(r)] for j in range(c)]
    # for i in range(r):
    #     for j in range(c):
    #         transpose[j][i] = matrix[i][j]
    
    # return transpose

    # With List Comprehension:
    
    rows_count = len(matrix)
    column_length = len(matrix[0])
    
    result = [[matrix[i][j] for i in range(rows_count)] for j in range(column_length)] 
    
    return result


test_cases = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]]]
for test in test_cases:
    print(transpose(test))
        
        