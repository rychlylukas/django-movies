from django.urls import path

from movies import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('topten', views.topten, name='topten'),
]


