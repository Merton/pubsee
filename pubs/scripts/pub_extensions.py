from pubs.models import Pub
import math
def all_pubs():
    return Pub.objects.all()

def pub_by_id(pub_id):
    return Pub.objects.filter(pub_id = pub_id)

def pub_by_name(name):
    return Pub.objects.filter(name = name)

def pubs_by_area(area):
    return Pub.objects.filter(local_authority = area)
    
# returns all pubs within the given distance of the bearing points.
def pub_within(distance):
    lat1=50.761380
    long1=-1.297824
    near_pubs = []
    for pub in all_pubs():
        lat2=float(pub.latitude)
        long2=float(pub.longitude)
        pubdistance=calc_distance(lat1,long1,lat2,long2)
        if pubdistance<=distance:
            near_pubs.append(pub)
    return near_pubs

# calculates distance between two bearing points
def calc_distance(lat1,long1,lat2,long2):
    p = 0.017453292519943295;    # Math.PI / 180
    a = 0.5 - math.cos((lat2 - lat1) * p)/2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((long2 - long1) * p))/2
    return 12742 * math.asin(math.sqrt(a)) # 2 * R; R = 6371 km
