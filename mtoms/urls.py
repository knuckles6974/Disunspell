from django.urls  import path
from .views       import ActorView,MovieView ,MovieInfoView


urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view()),  
    path('/movieinfo',MovieInfoView.as_view()),
]