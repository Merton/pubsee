from pubs.models import Pub
from pub_extensions import *

def remove_bad_characters():
    for pub in all_pubs:
        area = list(pub.local_authority)
        char_pos=area.find("'")
        if char_pos != -1:
            print(area)
            del area[char_pos]
            area="".join(area)
            pub.local_authority=area
            p.save()
            print(pub.local_authority)


def run():
    remove_bad_characters()
