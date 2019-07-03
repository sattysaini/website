from . import views
from django.urls import path

app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),

    #/music/<album_id>
    path('<int:pk>/', views.DetailView.as_view(), name='details'),

    path('<int:pk>/favorite/', views.DetailView.as_view(), name='favorite'),

]