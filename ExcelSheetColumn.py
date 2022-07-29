def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while columnNumber:
            ans += letters[(columnNumber-1)%len(letters)]
            columnNumber=(columnNumber-1)//len(letters)
        return ans[::-1]
