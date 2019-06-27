from . import views
from django.urls import path

app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.index, name='index'),

    #/music/<album_id>
    path('<int:album_id>/', views.details, name='details'),

    #/music/<album_id>/favorite/
    path('<int:album_id>/favorite/', views.favorite, name='favorite')
]