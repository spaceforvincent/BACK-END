from django.urls import path
from . import views



urlpatterns = [
    path('review/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_update_delete),
]