from django.urls import path
from .views import ReviewList


urlpatterns = [
    path('list/', ReviewList.as_view(), name='reviews_list'),
]