from django import forms
from .models import Album,Song

class AddAlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields=('title','artist','genre','artwork')

class AddSongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=('file',)

