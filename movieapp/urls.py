from django.urls import path
from.import views
urlpatterns=[
    path('',views.movie,name="movie"),
    path('movie1/',views.movie1,name="movie1")
]