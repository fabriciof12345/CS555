
# Implemented in order to improve code legibility
# Improve optimaztion of code
# Format (YYYY,MM,DD)
def CenturyBabies(dateOfBirth):
    #Years
    birth_year = int(dateOfBirth[:len(dateOfBirth)-5])

    return birth_year % 10 == 0 and birth_year % 100 == 0


