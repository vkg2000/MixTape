
from django.urls import path

from . import views

app_name='music'

urlpatterns = [

	#/music/
    path("",views.IndexView.as_view(), name='index'),

    #/music/all_albums
    path("all_albums/",views.AlbumView.as_view(), name='album'),

    #/music/71/
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    path('album/add/',views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    path('album/<int:pk>/',views.AlbumUpdate.as_view(), name='album-update'),
    
    #/music/album/2/delete/
    path('album/<int:pk>/delete/',views.AlbumDelete.as_view(), name='album-delete'),

    #/music/1/fav/
    path(r'^(?P<song_id>[0-9]+)/fav/$', views.fav, name='fav'),
    
    #music/2/fav_album
    path(r'^(?P<album_id>[0-9]+)/fav_album/$', views.fav_album, name='fav_album'),


    #music/song/1/delete
    path('song/<int:pk>/delete/',views.SongDelete.as_view(), name='song-delete'),

    #music/song/add
    path('song/add/',views.SongCreate.as_view(), name='song-add'),

    #music/all_songs
    path("all_songs/",views.SongView.as_view(), name='allsongs'),

    #music/search
    path("search/",views.search, name='search'),


]


