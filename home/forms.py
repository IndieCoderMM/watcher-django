from django import forms
from .models import Character


class HeroForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'identity', 'origin', 'power', 'strength', 'height',
                  'combat', 'intelligence', 'team', 'story', 'image']
