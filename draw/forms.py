from django import forms
from .models import Draw


DRAW_CHOICES = [
    ('Team_X', 'Team_X'),
    ('Space_Place', 'Space_Place'),
    ('Mu', 'Mu'),
    ('Sof', 'Sof'),
    ('Arch', 'Arch'),
    ('Small_Space', 'Small_Space'),
    ('Nothing', 'Nothing')
]

class DrawForm(forms.ModelForm):
    class Meta:
        model = Draw
        fields = ['first', 'second', 'third']
        widgets = {
            'first': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
            'second': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
            'third': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
        }
        labels = {
            'first': '1지망',
            'second': '2지망',
            'third': '3지망',
        }
