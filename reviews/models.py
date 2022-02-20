from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


class Site(models.Model):

    domain = models.CharField(
        max_length=63,
        unique=True,
        validators=[
            RegexValidator(
                '^[a-z0-9]+\.[a-z]+$',
                message="Domain names can only use letters, and numbers"
                        "Domains cannot exceed 63 characters. "
            )
        ]
    )

    def __str__(self):
        return f'{self.domain}'


class Review(models.Model):

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.site} - {self.author}'
