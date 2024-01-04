class solution(object):
    def delvowels(self,s):
        s=s.replace("a","")
        s=s.replace("e","")
        s=s.replace("i","")
        s=s.replace("o","")
        s=s.replace("u","")
        return s
    chr=solution()
print(chr.delvowels(input("enter string:")))






