from django.urls import path
from .views import review_create, ReviewList, ReviewDetail, ReviewDelete, ReviewUpdate, review_search


urlpatterns = [
    path('create/', review_create, name='review_create'),
    path('list/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
    path('<int:pk>/update/', ReviewUpdate.as_view(), name='review_update'),
    path('<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    path('search/', review_search, name='review_search'),
]
