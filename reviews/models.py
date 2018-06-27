from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class Company(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    )

    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    ip_address = models.GenericIPAddressField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
