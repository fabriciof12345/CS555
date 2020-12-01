from datetime import datetime
from dateutil.relativedelta import relativedelta


def childbirthsOnMarriage(famDICT,Indi_DICT):
    children = []
    children_birth = []
    marrigeDate = []
    marDate = False
    birth_cond = True
    for fam in famDICT.values():
        for a in fam:
            if marDate:
                marrigeDate.append(datetime.strptime(a[1], "%d %b %Y"))
                marDate = False
            if a[0] == 'MARR':
                marDate = True
        for i in fam:
            if i[0] == 'CHIL':
                children.append(Indi_DICT.get(i[1]))
        for j in children:
            children_birth.append(datetime.strptime(j[2], "%d %b %Y"))
        for k in children_birth:
            if abs((k.year - marrigeDate[0].year) * 12 + (k.month - marrigeDate[0].month)) == 0 and abs((k - marrigeDate[0]).days) == 0:
                birth_cond = False
        children_birth = []
        children = []
    return birth_cond