from .models import Album, Song
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


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album': album,
            'error_message': "You did not have any favorite song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})