def num_of_paths_to_dest(n):
    ways = [[0 for _ in range(n)] for _ in range(n)]

    ways[0][0] = 1

    for row in range(n):
        for col in range(row, n):
            leftX, leftY = getLeftCoords(row, col)
            bottomX, bottomY = getBottomCoords(row, col)

            if isWhiteSquare(leftX, leftY, ways):
                ways[row][col] += ways[leftX][leftY]

            if isWhiteSquare(bottomX, bottomY, ways):
                ways[row][col] += ways[bottomX][bottomY]

    return ways[n-1][n-1]


def getLeftCoords(row, col):
    return row-1, col


def getBottomCoords(row, col):
    return row, col-1


def isWhiteSquare(row, col, ways):
    return 0 <= row < len(ways) and row <= col < len(ways[0])
