from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Review


class ReviewList(ListView):
    model = Review
    template_name = 'reviews/list.html'

class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews/detail.html'
