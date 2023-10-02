from django.shortcuts import render, redirect
from .models import Movies, ThingsILike

def home(request):
  movies = Movies.objects.all()
  things = ThingsILike.objects.all()
  
  return render(request, "home.html", context={ 
    "mvs": movies,
    "things": things
  })

def create_movie(request):
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    Movies.objects.create(
      title = request.POST["title"],
      director = request.POST["director"],
      genre = request.POST["genre"],
      release_date = request.POST["release_date"]
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

def update_movie(request, id):
  movie = Movies.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    movie.title = request.POST["title"]
    movie.director = request.POST["director"]
    movie.genre = request.POST["genre"]
    movie.release_date = request.POST["release_date"]
    movie.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","movie": movie})

def delete_movie(request, id):
  movie = Movies.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      movie.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"movie": movie})