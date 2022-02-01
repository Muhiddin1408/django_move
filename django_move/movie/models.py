from datetime import date

from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Actor va rejissor'
        verbose_name_plural = 'Actor va rejissor'


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Janr'
        verbose_name_plural = 'Janri'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='Actor va rejissor', related_name='directors')
    actors = models.ManyToManyField(Actor, verbose_name='Actor va rejissor', related_name='actors')
    genres = models.ManyToManyField(Genre, verbose_name='Janr')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='eaerfgg')
    fees_in_us = models.PositiveIntegerField(default=0, help_text='uibnbub')
    fees_in_world = models.PositiveIntegerField(default=0, help_text='bkhbhk')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'film'


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "star of ruiting"
        verbose_name_plural = "star of ruiting"
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='movie', related_name='ratings')

    def __str__(self):
        return f"{self.star}-{self.movie}"

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    movie = models.ForeignKey(Movie, verbose_name='film', on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return f"{self.name}-{self.name}"

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'review'


