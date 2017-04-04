from django import forms
from .models import Album,Song

class AddAlbumForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'title',
        'class': 'form-control',

    }))
    artist = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'artist',
        'class': 'form-control',

    }))

    genre = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'genre',
        'class': 'form-control',

    }))

    class Meta:
        model=Album
        fields=('title','artist','genre')

class AddSongForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'id': 'song',
        'class': 'form-control',
        'accept': '.mp3,.m4a'

    }))
    class Meta:
        model=Song
        fields=('file',)

