from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()

class AlbumView(generic.ListView):
    template_name = 'music/all_album.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model=Album
	fields=['artist','album_title','year','album_logo' ,'is_fav']


class AlbumUpdate(UpdateView):	
	model=Album
	fields=['artist','album_title','year','album_logo']	

		
class AlbumDelete(DeleteView):
    model = Album
    success_url=reverse_lazy('music:index')
			

def fav_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_fav:
            album.is_fav = False
        else:
            album.is_fav = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return HttpResponseRedirect(reverse("music:index",
            ))

def fav(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_fav:
            song.is_fav = False
        else:
            song.is_fav = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	
		
class SongDelete(DeleteView):
    model = Song
    def get_success_url(self):
        return reverse_lazy('music:detail', kwargs={'pk': self.object.album.id})


class SongCreate(CreateView):
	model=Song
	fields=['album','song_title','audio_file','file_type', 'is_fav']



class SongView(generic.ListView):
    template_name = 'music/allsongs.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()




def search(request):
    query = request.GET['query']
    if query:
        all_albums = Album.objects.filter(album_title__icontains=query)
        all_songs = Song.objects.filter(song_title__icontains=query)
        params = {'all_albums':all_albums,'all_songs':all_songs}
        return render(request,'music/search.html', params)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


            