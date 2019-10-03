import copy

def get_perm(s):
    ls = list(s)
    ls_temp = [[]]
    el_1 = None
    for elem in ls:
        # ls_temp.append([elem])
        for el in ls_temp:
            if len(el)>0:
                el_1 = copy.deepcopy(el)
                for i in range(len(el_1)):
                    el_1.insert(i,elem)
                el.append(elem)
        ls_temp.append([elem])
        if el_1 is not None:
            ls_temp.append(el_1)
    return ls_temp

print(get_perm('abc'))


