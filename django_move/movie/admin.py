from django.contrib import admin
from .models import Movie, Category, Actor, Genre, Review, Rating, RatingStar

# Register your models here.

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(RatingStar)
