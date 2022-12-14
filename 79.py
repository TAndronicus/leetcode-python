from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.exists(board, [[i, j]], [i, j], word[1:]):
                    return True
        return False

    def exists(self, board: List[List[str]], visited: List[List[int]], position: List[int], strLeft: str):
        if len(strLeft) == 0:
            return True
        if position[0] > 0:
            newPosition = [position[0] - 1, position[1]]
            if board[newPosition[0]][newPosition[1]] == strLeft[0] and newPosition not in visited and self.exists(board, visited + [newPosition],
                                                                                                                  newPosition, strLeft[1:]):
                return True
        if position[0] < len(board) - 1:
            newPosition = [position[0] + 1, position[1]]
            if board[newPosition[0]][newPosition[1]] == strLeft[0] and newPosition not in visited and self.exists(board, visited + [newPosition],
                                                                                                                  newPosition, strLeft[1:]):
                return True
        if position[1] > 0:
            newPosition = [position[0], position[1] - 1]
            if board[newPosition[0]][newPosition[1]] == strLeft[0] and newPosition not in visited and self.exists(board, visited + [newPosition],
                                                                                                                  newPosition, strLeft[1:]):
                return True
        if position[1] < len(board[0]) - 1:
            newPosition = [position[0], position[1] + 1]
            if board[newPosition[0]][newPosition[1]] == strLeft[0] and newPosition not in visited and self.exists(board, visited + [newPosition],
                                                                                                                  newPosition, strLeft[1:]):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(not s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCS"))
    print(not s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCS"))
