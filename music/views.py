from django.shortcuts import render ,get_object_or_404,redirect,reverse
from .models import Album,Song
# from django.views import generic
from .forms import AddAlbumForm,AddSongForm
from .metatags import get_tags_info
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#




# Create your views here.
@login_required(login_url='/accounts/login')
def all_albums(request):
  albums=Album.objects.filter(uploader=request.user)
  return render(request, 'albums.html', {'albums':albums})

@login_required(login_url='/accounts/login')
def all_songs(request):
    albums=Album.objects.filter(uploader=request.user)
    songs=Song.objects.filter(album=albums)
    return render(request,'songs.html',{'songs':songs})

@login_required(login_url='/accounts/login')
def album_detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id,uploader=request.user)
    return render(request,'detail.html',{'album':album})



@login_required(login_url='/accounts/login')
def add_album (request):
    if request.method=='POST':
        form=AddAlbumForm(request.POST,request.FILES)
        if form.is_valid():
            album=form.save(commit=False)
            album.uploader=request.user
            album.save()
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

    try:
        Album.objects.get(pk=album_id,uploader=request.user).delete()

    except  :
        messages.warning(request,'Sorry, you do not have authority to delete this album...')
        return redirect('home')
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



