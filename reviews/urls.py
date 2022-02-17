from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate, ReviewDelete


urlpatterns = [
    path('create/', ReviewCreate, name='review_create'),
    path('list/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
    path('<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
