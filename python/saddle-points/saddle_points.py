def saddle_points(matrix):
    """Returns the indices of saddle points in given matrix."""
    if matrix != [] and any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Irregular matrix")

    points = []
    indices = [(i,j)
            for i in range(len(matrix))
            for j in range(len(matrix[j]))
            ]

    for i, j in indices:
        if _is_saddle_point(matrix[i][j], matrix[i], _column(matrix, j)):
            points.append({"row": i+1, "column": j+1})

    return points


def _column(matrix: list, indic: int) -> list:
    return [row[indic] for row in matrix]


def _is_saddle_point(element: int, row: list, column: list) -> bool:
    return element == max(row) and element == min(column)
