from pubs.models import Pub
import csv
def readPubs():
    file = open("open_pubs.csv", "r")
    reader = csv.reader(file)
    count = 0
    for record in reader:
        p = Pub()
        p.pub_id = record[0]
        p.name = record[1]
        p.address = record[2]
        p.postcode = record[3]
        p.easting = record[4]
        p.northing = record[5]
        try:
          p.latitude = float(record[6])
        except ValueError:
          p.latitude = 0
          print("Error in converting latitude from a string")
        try:
          p.longitude = 0
          p.longitude = float(record[7])
        except ValueError:
          print("Error in converting longitude from a string")
        p.local_authority = record[8]
        p.save()



def run():
    readPubs()
