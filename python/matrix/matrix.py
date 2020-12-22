class Matrix:
    """Matrix(matrix_string) -> new Matrix object"""
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()]
                for row in matrix_string.splitlines()]

    def row(self, index):
        """Return the row at index as a list."""
        return self.matrix[index - 1].copy()

    def column(self, index):
        """Return the column at index as a list."""
        return [row[index -1] for row in self.matrix]
