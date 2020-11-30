def retrieveInfo():
    nameAge = []
    with open("Tables.txt") as output:
        lines = output.readlines()
        end = lines.index("Families\n") - 1
        for x in range(4, end):
            name = lines[x].split("|")[2].replace(" ","").replace("/"," ").rstrip()
            age = lines[x].split("|")[5].replace(" ","").replace("/"," ").rstrip()
            nameAge.append([name,age])
        return nameAge

def eldestIndividual(listOfNameAges):
    if listOfNameAges == []:
        return False
    eldestIndex = 0
    eldest = 0
    for x in range(len(listOfNameAges)):
        if listOfNameAges[x][1] > eldest:
            eldest = listOfNameAges[x][1]
            eldestIndex = x
    return (listOfNameAges[eldestIndex])
