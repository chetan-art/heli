from django.forms import ModelForm
from home.models import Polymodel
class polygonform(ModelForm):
    class Meta:
        model = Polymodel
        fields = ['polygon1','polygon2']