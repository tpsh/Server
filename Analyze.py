from pandas import *
def FindMean(z):
    aa = dict.fromkeys(list(z[0].keys()))
    for k in range(0, len(z[0])):
        aa[list(z[0].keys())[k]] = []

    for i in z:
        for k in range(0, len(i)):
            aa[list(i.keys())[k]].append(i[list(i.keys())[k]])
    tab = DataFrame(aa)
    return dict(tab.mean())