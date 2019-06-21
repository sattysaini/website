from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
#from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = { 'all_albums' : all_albums }
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)


def details(request, album_id):
    return HttpResponse("<h1> Here is the Album " + str(album_id) + "</h1>")