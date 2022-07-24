def transpose(self,a, n):
        for i in range(n):
            for j in range(i,n):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        return a
