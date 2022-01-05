from django.forms import ModelForm, inlineformset_factory

from .models import Monster, SpecialAttack


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = ("name", "treat_like", "description", "image")


SpecialAttackFormSet = inlineformset_factory(
    Monster,
    SpecialAttack,
    fields=("name", "description"),
    extra=1,
)
