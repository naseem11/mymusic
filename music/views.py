from django.shortcuts import render ,get_object_or_404,redirect,reverse
from .models import Album,Song
# from django.views import generic
from .forms import AddAlbumForm,AddSongForm
from .metatags import get_tags_info
from django.contrib.auth.decorators import login_required
#




# Create your views here.
@login_required(login_url='/accounts/login')
def all_albums(request):
  albums=Album.objects.all()
  return render(request, 'albums.html', {'albums':albums})

@login_required(login_url='/accounts/login')
def all_songs(request):
    songs=Song.objects.all()
    return render(request,'songs.html',{'songs':songs})

@login_required(login_url='/accounts/login')
def album_detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'detail.html',{'album':album})

@login_required(login_url='/accounts/login')
def add_album (request):
    if request.method=='POST':
        form=AddAlbumForm(request.POST,request.FILES)
        if form.is_valid():
            album=form.save()
            return redirect('detail',album.pk)
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
    Album.objects.get(pk=album_id).delete()
    return redirect('home')

@login_required(login_url='/accounts/login')
def delete_song(request,song_id):
     song_to_delete=Song.objects.get(pk=song_id)
     album_of_that_song=song_to_delete.album.id
     song_to_delete.delete()
     return redirect('detail',album_of_that_song)




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



