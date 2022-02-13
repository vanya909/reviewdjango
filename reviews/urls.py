from django.urls import path
from .views import ReviewList, ReviewDetail


urlpatterns = [
    path('list/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
