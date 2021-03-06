from django.conf import settings
from django.db import models
from django.urls import reverse


class Monster(models.Model):
    name = models.CharField(max_length=50)
    treat_like = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=5_000)
    image = models.ImageField(upload_to="monsters", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="monsters"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_date",)

    def get_absolute_url(self):
        return reverse("monsters-monster_detail", kwargs={"monster_id": self.id})

    def __str__(self):
        return self.name

    def get_short_description(self, length=500):
        if len(self.description) > length:
            return self.description[: length - 1] + "…"
        return self.description


class SpecialAttack(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1_000)
    monster = models.ForeignKey(
        Monster, on_delete=models.CASCADE, related_name="special_attacks"
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_date",)

    def __str__(self):
        return self.name
