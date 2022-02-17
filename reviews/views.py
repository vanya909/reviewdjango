from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Review, Site
from .forms import ReviewCreationForm


class ReviewList(ListView):
    model = Review
    template_name = 'reviews/list.html'


class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews/detail.html'


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/delete.html'
    success_url = reverse_lazy('review_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url='/users/login/')
def ReviewCreate(request):
    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.site, created = Site.objects.get_or_create(domain=form.cleaned_data['site_name'])
            review.author = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewCreationForm()
    return render(request, 'reviews/create.html', context={'form': form})
