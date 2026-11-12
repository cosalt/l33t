def solution(N):
    n = bin(N)[2:]
    n = str(n).split("1")[1:-1]
    n = [i for i in n if i != ""]
    n.sort()
    if len(n) == 0:
        return 0 
    else:
        return len(n[-1])
