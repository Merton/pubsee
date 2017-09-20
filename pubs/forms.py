from django.forms import ModelForm
from . models import Pub

class PubForm(ModelForm):
    class Meta:
        model = Pub
        fields =['pub_id','name','address','postcode','latitude','longitude','local_authority']
    def process(self):
        cd = self.cleaned_data
