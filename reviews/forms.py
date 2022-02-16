from django import forms
from django.core.validators import RegexValidator
from .models import Review


class ReviewCreationForm(forms.ModelForm):
    site_name = forms.CharField(
        help_text="e.g. google.com",
        max_length=63,
        validators=[
            RegexValidator(
                '^[a-z0-9][a-z0-9\-]+[a-z0-9]\.[a-z]+$',
                message="Domain names can only use letters, " +
                        "numbers and hyphens (“-“). " +
                        "Names cannot begin or end with a hyphen. " +
                        "Domains cannot exceed 63 characters. " +
                        "Domain name can only contains at least 3 characters."
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
