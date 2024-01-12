from django.shortcuts import render,redirect
from .models import song,artist
# Create your views here.

def home(req):

    return render(req,'index.html')

def all_songs(req):
    all_songs = song.objects.prefetch_related('artists').all()

    return render(req,'songs.html',{'all_songs':all_songs})

def create_song(req):
    if req.method  == "POST":
        
        title = req.POST['title']
        artist_name = req.POST['names']
        print("i am inaise trhe create song")
        new_artist = artist.objects.create(name = artist_name)
        new_artist.save()
        new_song = song.objects.create(title= title)
        new_song.artists.add(new_artist)
        new_song.save()

    return render(req,'index.html')
