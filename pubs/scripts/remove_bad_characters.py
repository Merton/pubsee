from pubs.models import Local_Authority
# from pub_extensions import all_pubs
def remove_bad_characters():
    for local_authority in Local_Authority.objects.all():
        local_authority.name.replace("'", "")
        local_authority.save()

def run():
    remove_bad_characters()
