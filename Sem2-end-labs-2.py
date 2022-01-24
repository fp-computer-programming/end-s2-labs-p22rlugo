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
            