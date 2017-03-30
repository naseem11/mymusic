from django.conf.urls import url
from .views import all_albums,album_detail,add_album,add_song,all_songs,delete_album,delete_song


urlpatterns = [

     url(r'^$', all_albums , name='home'),
     url(r'^(?P<album_id>[0-9]+)/$',album_detail, name='detail'),
     url(r'^add/$',add_album,name='addalbum'),
     url(r'^(?P<album_id>[0-9]+)/addsong/$', add_song,  name='addsong'),
     url(r'^tracks/$', all_songs, name='allsongs'),
     url(r'^delete/(?P<album_id>[0-9]+)/$', delete_album, name='deletealbum'),
     url(r'^deletesong/(?P<song_id>[0-9]+)/$',delete_song,name='deletesong')

]