from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'list/index.html', context)

def create(request):
    movie = Movie(title=request.POST['title'], director=request.POST['director'], genre=request.POST['genre'])
    movie.save()
    return redirect('/')

def edit(request, id):
    movies = Movie.objects.get(id=id)
    context = {'movies': movies}
    return render(request, 'list/edit.html', context)

def update(request, id):
    movie = Movie.objects.get(id=id)
    movie.title = request.POST['title']
    movie.director = request.POST['director']
    movie.genre = request.POST['genre']
    movie.save()
    return redirect('/list/')

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/list/')
