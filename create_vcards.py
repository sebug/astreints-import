import csv
import vobject

class Astreint:
    """Somebody conscripted to civil protection"""
    def __init__(self, row):
        self.name = row[0]
        self.first_name = row[1]
        self.function = row[2]
        self.phone = row[3]

    def as_vcard(self):
        j = vobject.vCard()
        j.add('n')
        j.n.value = vobject.vcard.Name( family = self.name, given = self.first_name)
        j.add('fn')
        j.fn.value = self.first_name + ' ' + self.name
        tel = j.add('tel')
        tel.type_param = "home"
        tel.value = self.phone
        return j


with open('astreints.csv', newline='') as csvfile:
    astreintsreader = csv.reader(csvfile, delimiter=';')
    astreintsreader.__next__() # skip header
    astreints = map(Astreint, astreintsreader)
    astreints_with_phone = filter(lambda a: a.phone, astreints)
    with open('all.vcf', 'a') as all_cards:
        for astreint in astreints_with_phone:
            vc = astreint.as_vcard()
            all_cards.write(vc.serialize())

        



