from django.shortcuts import render
from django.views.generic import ListView

from .models import Review


class ReviewList(ListView):
    model = Review
    template_name = 'reviews/list.html'
