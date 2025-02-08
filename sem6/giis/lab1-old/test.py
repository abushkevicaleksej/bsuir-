def multiply_matrices(mtx1, mtx2):
    rows_mtx1 = len(mtx1)
    cols_mtx1 = len(mtx1[0])
    rows_mtx2 = len(mtx2)
    cols_mtx2 = len(mtx2[0])

    if cols_mtx1 != rows_mtx2:
        raise ValueError("Невозможно умножить матрицы: количество столбцов первой матрицы "
                         "должно совпадать с количеством строк второй матрицы.")

    result = [[0 for _ in range(cols_mtx2)] for _ in range(rows_mtx1)]

    for i in range(rows_mtx1):
        for j in range(cols_mtx2):
            result[i][j] = sum(mtx1[i][k] * mtx2[k][j] for k in range(cols_mtx1))

    return result

if __name__ == '__main__':
    points = []
    for i in range(0, 11):
        t = i / 10.0
        p1 = [0, 0]
        p2 = [1, 0]
        r1 = [0, 1]
        r2 = [1, 0]

        mtx = [
            [p1[0], p1[1]],
            [p2[0], p2[1]],
            [r1[0], r1[1]],
            [r2[0], r2[1]]
        ]

        default_mtx = [
            [2, -2, 1, 1],
            [-3, 3, -2, -1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]

        temp_mtx = multiply_matrices(default_mtx, mtx)
        t_mtx = multiply_matrices([[t ** 3, t ** 2, t, 1]], temp_mtx)

        points.append((t_mtx[0][0], t_mtx[0][1]))
        print(points)