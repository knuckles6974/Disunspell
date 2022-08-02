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
            date_of_birth=data["date_of_birth"],

        )


        return JsonResponse({"message": "배우정보 등록완료"}, status=201)

class MovieView(View):
    def post(self, request):
        
        input_data = json.loads(request.body)
        
        Movie.objects.create(
            title = input_data['title'],
            release_date = input_data['release_date'],
            running_time = input_data['running_time'],
            
        )
        
        return JsonResponse({"message": "영화정보등록완료"}, status=201)    
                
            
class MovieInfoView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            actormovies = actor.actormovies.all()	
            movie_list = []
            for actormovie in actormovies:
                movie_info = {
                    "title": actormovie.movie.title,
                }
                movie_list.append(movie_info)
            results.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "title": movie_list,
                }
            )
        return JsonResponse({"results": results}, status=200)