from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('movie/', views.MovieViewSet.as_view({'get': 'list'})),
    path('movie/<int:pk>/', views.MovieViewSet.as_view({'get': 'retrieve'})),
    path('review/', views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path('rating/', views.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('actors/', views.ActorViewSet.as_view({'get': 'list'})),
    path('actors/<int:pk>/', views.ActorViewSet.as_view({'get': 'retrieve'})),

])
