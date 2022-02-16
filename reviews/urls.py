from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate


urlpatterns = [
    path('create/', ReviewCreate, name='create'),
    path('list/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
