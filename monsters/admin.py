from django.contrib import admin

from .models import Monster, SpecialAttack


class SpecialAttackInline(admin.StackedInline):
    model = SpecialAttack


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    inlines = [SpecialAttackInline]
