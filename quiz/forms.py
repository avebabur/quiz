from .models import Flag
from django.forms import ModelForm

class FlagForm(ModelForm):
    class Meta:
        model = Flag
        fields = '__all__'