from django import forms
from django.core.validators import RegexValidator
from .models import Review


class ReviewCreationForm(forms.ModelForm):
    site_name = forms.CharField(
        help_text="e.g. google.com",
        max_length=63,
        validators=[
            RegexValidator(
                '^[a-z0-9]+\.[a-z]+$',
                message="Domain names can only use letters, and numbers"
                        "Domains cannot exceed 63 characters. "
            )
        ]
    )

    class Meta:
        model = Review
        fields = ['rating', 'description']
        help_texts = {
            'rating': 'From 0 to 5',
        }

    field_order = ['site_name', 'rating', 'description']
