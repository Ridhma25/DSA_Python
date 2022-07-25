def lengthOfLastWord(self, s: str) -> int:
    l = []
    for i in s:
        l.append(s.split())
     s1 = l[0]
     return len(s1[len(s1)-1])
