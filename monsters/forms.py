from django.forms import ModelForm

from .models import Monster


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = ("name", "treat_like", "description", "image")
