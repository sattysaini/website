from .models import Album
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { 'all_albums' : all_albums })       #render = HttpResponse + template.loader + template.render
    # template = loader.get_template('music/index.html')
    # return HttpResponse(template.render(context, request))


def details(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    #try:
    #    album = Album.objects.get(pk = album_id)
    #except Album.DoesNotExist :
    #    raise Http404("Album does not exist")
    return render(request, 'music/details.html', {'album': album})
    #return HttpResponse("<h1> Here is the Album " + str(album_id) + "</h1>")
