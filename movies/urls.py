from django.urls import path

from movies import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('films/genres/<str:genre_name>/', views.FilmListView.as_view(), name='film_genre'),
    path('topten', views.topten, name='topten'),
]