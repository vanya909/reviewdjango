from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Review, Site
from .forms import ReviewCreationForm


class ReviewList(ListView):
    model = Review
    template_name = 'reviews/list.html'


class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews/detail.html'


@login_required(login_url='/users/login/')
def ReviewCreate(request):
    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.site, created = Site.objects.get_or_create(domain=form.cleaned_data['site_name'])
            review.author = request.user
            review.save()
            return redirect('home')
    else:
        form = ReviewCreationForm()
    return render(request, 'reviews/create.html', context={'form': form})
