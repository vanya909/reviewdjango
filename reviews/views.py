from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
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


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'description']
    template_name = 'reviews/update.html'

    def get_success_url(self):
        return reverse_lazy('review_detail', args=[self.object.pk, ])

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url='/users/login/')
def review_create(request):
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


def review_search(request):
    searched = request.POST['searched']
    sites = Site.objects.filter(domain__contains=searched)
    review_list = []
    for site in sites:
        review_list += site.review_set.all()

    return render(
        request,
        'reviews/search.html',
        {'searched': review_list}
    )
