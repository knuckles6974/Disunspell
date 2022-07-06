import json
from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View
from .models          import Actor, Movie

# Create your views here.


class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)

        Actor.objects.create(

            first_name = data['first_name'],
            last_name  = data['last_name'],
            birth = data['birth'],

        )


        return JsonResponse({"message": "배우정보 등록완료"}, status=201)

class MovieView(View):
    def post(self, request):
        
        input_data = json.loads(request.body)
        
        Movie.objects.create(
            name = input_data['name'],
            release_date = input_data['release_date'],
            running_time = input_data['running_time'],
            
        )
        
        return JsonResponse({"message": "영화정보등록완료"}, status=201)    
                
            
class MovieInfoView(View):
    def get(self,request): 
        actors = Actor.objects.all()
        movie_info = Movie.objects.all()
        result = []
        for actor in actors:
            movies = actor.movie.all()
            movie_list = []
        
            for movie in movies: 
                    movie_info = {
                    "name" : [movie.name for actor.movies in actors],
                    "release_date" : actor.movie.release_date,
                    "running_time" : actor.movie.running_time
                    }
            movie_list.append(movie_info)
                
            result.append(
                {
                
                    "first_name" : actor.first_name,
                    "last_name"  : actor.last_name
                
                }
            )
        return JsonResponse({"영화정보" : result}, status=200)