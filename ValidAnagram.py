def isAnagram(self, s: str, t: str) -> bool:
        flag = 0
        tim = list(t)
        sim = list(s)
        for i in tim:
            if i in sim:
                flag = 1
                sim.remove(i)
            else:
                flag = 0
                break
        if flag==1 and len(s)<=len(t):
            return True
        else:
            return False
