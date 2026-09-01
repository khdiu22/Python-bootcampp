from django.shortcuts import render

movies = [
    {"id": 1, "title": "The good father", "year": 1972, "rating": 8.8},
    {"id": 2, "title": "The Dark Knight", "year": 2008, "rating": 8.9},
    {"id": 3, "title": "The Lion King", "year": 1994, "rating": 8.5},
]

def movie_list(request):
    return render(request, 'movies/movie_list.html', {'movies': movies})
def movie_detail(request, id):
    movie = movies[id - 1]
    return render(request, 'movies/movie_detail.html', {'movie': movie})