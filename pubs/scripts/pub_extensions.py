from pubs.models import Pub
# import Math

def all_pubs():
    return Pub.objects.all()

def pub_by_id(pub_id):
    return Pub.objects.filter(pub_id = pub_id)

def pub_by_name(name):
    return Pub.objects.filter(name = name)

# returns all pubs within the given distance of the bearing points.
def pub_within(lat, long, distance):
    near_pubs = []
    for pub in all_pubs():
        lat2=pub.latitude
        long2=pub.longitude
        if distance(lat,long,lat2,long2) >=distance:
            near_pubs.append(pub)
    return near_pubs

# calculates distance between two bearing points
def distance(lat1,long1,lat2,long2):
    p = 0.017453292519943295;    # Math.PI / 180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((long2 - long1) * p))/2
    return 12742 * asin(sqrt(a)) # 2 * R; R = 6371 km
