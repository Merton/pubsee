from pubs.models import Pub, Local_Authority
from django.db import models
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
          p.longitude = float(record[7])
        except ValueError:
          p.longitude = 0
          print("Error in converting longitude from a string")
        try:
            l = Local_Authority.objects.get(name=record[8])
        except :
            l = Local_Authority()
            l.name = record[8]
            l.save()
        p.local_authority = l
        p.save()
        count+=1
        print(count)

def run():
    readPubs()
