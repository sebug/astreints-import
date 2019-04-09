import csv
with open('astreints.csv', newline='') as csvfile:
    astreintsreader = csv.reader(csvfile, delimiter=';')
    for row in astreintsreader:
        print(', '.join(row))



