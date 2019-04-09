import csv

class Astreint:
    """Somebody conscripted to civil protection"""
    def __init__(self, row):
        self.name = row[0]
        self.first_name = row[1]
        self.function = row[2]
        self.phone = row[3]


with open('astreints.csv', newline='') as csvfile:
    astreintsreader = csv.reader(csvfile, delimiter=';')
    astreintsreader.__next__() # skip header
    astreints = map(Astreint, astreintsreader)
    astreints_with_phone = filter(lambda a: a.phone, astreints)
    for astreint in astreints_with_phone:
        print(astreint.phone)
        



