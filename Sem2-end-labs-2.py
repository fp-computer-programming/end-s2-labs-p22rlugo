# Ryan Lugo: RJL 1/24/22

def solution(n,d):
    table = list(str(n))
    for i,v in enumerate(table):
            table[i] = int(v)
    if d > len(table):
        return table
    elif d <= 0:
        return []
    else:
        return table[-d:]
            
print(solution(1,1) == [1])
print(solution(1234,2) == [3,4])
print(solution(637547,6) == [6, 3, 7, 5, 4, 7])