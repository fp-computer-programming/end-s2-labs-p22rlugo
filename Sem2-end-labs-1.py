# Ryan Lugo: RJL 1/24/22

def double_every_other(lst):
    if type(lst) == list:
        for i,v in enumerate(lst):
            if not i % 2== 0:
                lst[i]= v * 2
    return lst