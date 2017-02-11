from django.forms import ModelForm
from .models import Game

class addgame_form(ModelForm):
    class Meta:
        model = Game
        exclude = ['Created','Raters','Ratingsum','Rating']
