class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        n = str(n).split("1")[1:-1]
        if len(n) == 0:
            return 0 
        else:
            n.sort()
            return len(n[-1])+1
