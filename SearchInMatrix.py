def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = 0
        for i in range(len(matrix)):
            for j in range((len(matrix[i]))):
                if target == matrix[i][j]:
                    flag = 1
                    break
        if flag == 1:
            return True
        else:
            return False
