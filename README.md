![index_page](https://cloud.githubusercontent.com/assets/22799847/26198609/930ac5aa-3bbe-11e7-8e83-b2f006c7cd74.PNG)

# What is MyMusic?

MyMusic is web application which allows users to upload, store, and play  their music from the cloud. Music can be managed and listened to, from any device over the internet . An user can  access  only  his/her uploaded music.

## How does it work?

This application can be used by registered users only.So after signing up you can start adding your music .

### Adding a new album

To create a new album user needs to specify the title , artist and genre of the album, with this information , application goes to 'lastfm' to pull the artwork(cover) of the album.If the album does not exist on  lastfm , artwork is updated with a default artwork.

![addalbum_page](https://cloud.githubusercontent.com/assets/22799847/26198799/66f91060-3bbf-11e7-9206-6e64ba765cde.PNG)

![home_page](https://cloud.githubusercontent.com/assets/22799847/26198802/66fcbbd4-3bbf-11e7-9030-940273a57448.PNG)

### Adding a track

Just click on the album ,you want to add a new track to.You will be redirected to that album page there 'add track' button can be clicked to add a new track to that album.

![detail_page](https://cloud.githubusercontent.com/assets/22799847/26198803/66fcb97c-3bbf-11e7-822c-bde789479dd8.PNG)

user just need to select the track to add , track's information like title and duration of the track is retreived by processing the meta data of the track.

![addsong_page](https://cloud.githubusercontent.com/assets/22799847/26198801/66fc4190-3bbf-11e7-99da-0e8389d1785a.PNG)

## Searching

Music can be searched by artist , by album , by genre or by track.

![search_result](https://cloud.githubusercontent.com/assets/22799847/26198800/66f9e300-3bbf-11e7-83e2-429c404a82c5.PNG)

# Tecknologies used

## Client Side

**languages :** HTML, CSS, JavaScript

**Framework and Library :** Bootstrap, Jquery

## Server Side 

**Language :** Python

**Framework :** Django

**Packages :** 
* **hsaudiotag** - to process the meda data of audio files
* **django-cleanup** - for automatic cleanup of FileField and ImageField
* **django-gravatar2** 
* **Pillow** , and some more..

**API :** Last.fm api to get the album artwork (cover)

## Storage

**Database :** PostgreSQL

**Cloud Storage :** Amazon S3 bucket - to store all the static and media files

**Hosting :** Heroku


