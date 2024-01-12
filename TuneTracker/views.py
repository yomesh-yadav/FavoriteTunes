from django.shortcuts import render
from .models import song
# Create your views here.

def home(req):

    return render(req,'index.html')

def all_songs(req):
    all_songs = song.objects.prefetch_related('artists').all()

    return render(req,'songs.html',{'all_songs':all_songs})
