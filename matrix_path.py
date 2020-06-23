import numpy as np


class Solution:
    def exist(self, board, word):
        length = len(word)
        rows = len(board)
        cols = 0
        if board:
            cols = len(board[0])
        print('board', board)
        print('length', length)
        print('rows', rows)
        print('cols', cols)
        if not board or length < 0 or rows < 1 or cols < 1:
            return False

        visited = np.full(shape=(rows, cols), fill_value=0)
        pathLength = 0

        for row in range(rows):
            for col in range(cols):
                if self.hasPath(board, rows, row, cols, col, word, visited, pathLength):
                    return True

        del visited
        return False

    def hasPath(self, board, rows, row, cols, col, word, visited, pathLength):
        if pathLength == len(word):
            return True

        findPath = False

        if row >= 0 and row < rows and col >= 0 and col < cols and board[row][col] == word[pathLength] and \
                visited[row][col] == 0:
            print(word[pathLength])
            pathLength += 1
            visited[row][col] = 1

            findPath = self.hasPath(board, rows, row - 1, cols, col, word, visited, pathLength) or \
                       self.hasPath(board, rows, row, cols, col - 1, word, visited, pathLength) or \
                       self.hasPath(board, rows, row + 1, cols, col, word, visited, pathLength) or \
                       self.hasPath(board, rows, row, cols, col + 1, word, visited, pathLength)

            if not findPath:
                pathLength -= 1
                visited[row][col] = 0

        return findPath


def main():
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))


if __name__ == '__main__':
    main()
