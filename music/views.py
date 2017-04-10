from django.shortcuts import render ,get_object_or_404,redirect
from .models import Album,Song
import os

from .forms import AddAlbumForm,AddSongForm
from .metatags import get_tags_info
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.core.files.base import ContentFile







# Create your views here.
@login_required(login_url='/accounts/login')
def all_albums(request):
  albums=Album.objects.filter(uploader=request.user)
  return render(request, 'albums.html', {'albums':albums})

@login_required(login_url='/accounts/login')
def all_songs(request):
    albums=Album.objects.filter(uploader=request.user)
    songs=[]
    for album in albums:
        list_of_songs=Song.objects.filter(album=album)
        for song in list_of_songs:
            songs.append(song)
    return render(request,'songs.html',{'songs':songs})

@login_required(login_url='/accounts/login')
def album_detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id,uploader=request.user)
    return render(request,'detail.html',{'album':album})



@login_required(login_url='/accounts/login')
def add_album (request):
    if request.method=='POST':
        form=AddAlbumForm(request.POST)
        if form.is_valid():
            album=form.save(commit=False)
            album.uploader=request.user


            try:
                api_key=os.environ.get('API_KEY')
                rquest=requests.get('http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key='+api_key+'&artist='+album.artist+'&album='+album.title+'&format=json')
                json_object=rquest.json()
                img_url=json_object['album']['image'][2]['#text']

                image_content = ContentFile(requests.get(img_url).content)
                album.artwork.save(album.title, image_content)
            except:

                img_url='https://s3-eu-west-1.amazonaws.com/sangeet-app/media/artworks/default_artwork.png'
                album.artwork.save(album.title,ContentFile(requests.get(img_url).content))

            album.save()
            return redirect('detail', album.pk)



    else:
        form=AddAlbumForm()
        return render(request,'add_album.html', {'form':form})

@login_required(login_url='/accounts/login')
def add_song(request,album_id):
    if request.method=='POST':
        form=AddSongForm(request.POST,request.FILES)
        if form.is_valid():
            song=form.save(commit=False)
            song.album=Album.objects.get(pk=album_id)
            audio_file=form.cleaned_data['file']
            tags=get_tags_info(audio_file)
            song.title=tags['title']
            song.duration=tags['duration']
            song.save()
            return redirect('detail',album_id)
    else:
        form=AddSongForm()
        return render(request,'add_song.html',{'form':form})

@login_required(login_url='/accounts/login')
def delete_album(request,album_id):

    try:
        Album.objects.get(pk=album_id,uploader=request.user).delete()

    except :
        pass
        # messages.warning(request,'Sorry, you do not have authority to delete this album...')

    return redirect('home')

@login_required(login_url='/accounts/login')
def delete_song(request,song_id):
     song_to_delete=Song.objects.get(pk=song_id)
     album_id_of_that_song=song_to_delete.album.id
     album=song_to_delete.album
     if(album.uploader==request.user):
         song_to_delete.delete()
         return redirect('detail',album_id_of_that_song)
     else:
         messages.warning(request, "Sorry, you can't delete that song.. ")
         return redirect('home')



       # album=get_object_or_404(Album,id=album_id)
       # return render(request,'detail.html',{'album':album})


# class HomeView(generic.ListView):
#     template_name = 'albums.html'
#     context_object_name = 'albums'
#
#     def get_queryset(self):
#         return Album.objects.all()
#
# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'detail.html'



