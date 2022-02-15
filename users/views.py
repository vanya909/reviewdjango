from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = NewUserForm()
    return render(request, 'users/register.html', context={'register_form': form})
