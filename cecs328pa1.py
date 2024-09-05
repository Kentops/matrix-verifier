def isValidGrid(matrix: list) -> bool:
    """Returns false if the input matrix contains duplicate integers in rows, columns, or quadrants.\n
    matrix - a matrix of integers. The matrix's dimensions are equal and powers of two."""
    #create sets
    quad_sets = [[set(),set()],[set(),set()]]
    size = len(matrix)
    row_sets=[set(element for element in matrix[i]) for i in range(size)]
    col_sets=[set(matrix[n][i] for n in range(size)) for i in range(size)]
    for i in range(size):
        for j in range(size):
            quad_sets[i//(len(matrix)//2)][j//(len(matrix)//2)].add(matrix[i][j])
    #Compare
    for i in range(size):
        if len(row_sets[i]) != size:
            return False
        elif len(col_sets[i]) != size:
            return False
    for i in range(2):
        for j in range(2):
            if len(quad_sets[i][j]) != (size//2)**2:
                return False
    #Everything is good
    return True
