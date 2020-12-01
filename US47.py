from gedcom.parser import Parser
from datetime import date
from prettytable import PrettyTable
from gedcom.element.element import Element
from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement

INDI_DICT = {}
INDI_TABLE = PrettyTable()
INDI_TABLE.field_names = ["ID", "Name", "Gender",
                          "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]


def print_under_6(tempDICT):
    child = ""
    for key, value in tempDICT.items():
        if value[3] < 6:
            INDI_DICT[key] = value

    for x, y in INDI_DICT.items():

        if "Y" in y:
            y.remove("Y")
            y.insert(4, False)
        else:
            y.insert(4, True)
            y.insert(5, "N/A")

        body = y[0:6]
        rel = y[6:]
        relations = []
        body.insert(0, x.replace("@", ""))
        spouse = []
        for z in rel:
            if isinstance(z, list):
                relations = z

        for i in range(len(relations)):
            child = relations[i].replace("@", "")
            if child == "N/A":
                if relations[1].replace("@", "") == "N/A":
                    spouse = []
                else:
                    spouse.append(relations[1].replace("@", ""))
            else:
                body.append(child)

        while len(body) != 8:
            body.append([])

        body.append(spouse)
        INDI_TABLE.add_row(body)

    print("\nIndividuals under 6")
    print(INDI_TABLE)
    return True
