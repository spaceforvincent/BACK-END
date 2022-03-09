from django.urls import path
from . import views

urlpatterns = [
    path('lotto/', views.lotto, name='lotto'),
]
