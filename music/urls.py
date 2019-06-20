from . import views
from django.urls import path

urlpatterns = [
    #/music/
    path('', views.index, name='index'),

    #/music/<album_id>
    path('<int:album_id>/', views.details, name='details')
]