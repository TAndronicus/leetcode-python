from typing import List


def reconstructRoutes(routeMatrix: List[List[str]], leftStr: str, routeSoFar: str, left: int, right: int) -> List[str]:
    if left == -1 or right == -1:
        return [routeSoFar]
    if routeMatrix[left][right] == 'L':
        return reconstructRoutes(routeMatrix, leftStr, routeSoFar, left - 1, right)
    if routeMatrix[left][right] == 'R':
        return reconstructRoutes(routeMatrix, leftStr, routeSoFar, left, right - 1)
    if routeMatrix[left][right] == 'B':
        return reconstructRoutes(routeMatrix, leftStr, routeSoFar, left - 1, right) + reconstructRoutes(routeMatrix, leftStr, routeSoFar, left,
                                                                                                        right - 1)
    if routeMatrix[left][right] == 'X':
        return reconstructRoutes(routeMatrix, leftStr, leftStr[left] + routeSoFar, left - 1, right - 1)


def needlemanWunsch(left: str, right: str) -> (List[str], int):
    maxLengths = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
    routes = [[''] * len(right) for _ in range(len(left))]
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] == right[j]:
                maxLengths[i + 1][j + 1] = maxLengths[i][j] + 1
                routes[i][j] = 'X'
            elif maxLengths[i][j + 1] == maxLengths[i + 1][j]:
                maxLengths[i + 1][j + 1] = maxLengths[i + 1][j]
                routes[i][j] = 'B'
            elif maxLengths[i][j + 1] > maxLengths[i + 1][j]:
                maxLengths[i + 1][j + 1] = maxLengths[i][j + 1]
                routes[i][j] = 'L'
            else:
                maxLengths[i + 1][j + 1] = maxLengths[i + 1][j]
                routes[i][j] = 'R'
    return reconstructRoutes(routes, left, '', len(left) - 1, len(right) - 1), maxLengths[len(left)][len(right)]


if __name__ == '__main__':
    print(needlemanWunsch("", "") == ([""], 0))
    print(needlemanWunsch("ABCABC", "CACBAC") == (["ABAC", "ACAC", "ACBC", "CABC"], 4))
