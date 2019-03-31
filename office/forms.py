from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'tittle', 'titttle','description']
        #fields = '__all__'
