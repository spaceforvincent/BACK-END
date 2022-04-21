from django.urls import path
from . import views


urlpatterns = [
    path('artist/', views.artist_list), #가수 정보 조회 및 생성
    path('artist/<int:artist_pk>/',views.artist_detail),
    path('artist/<int:artist_pk>/music/',views.music_create),
    path('music/', views.music_list),
    path('music/<int:music_pk>/',views.music_detail),
]
