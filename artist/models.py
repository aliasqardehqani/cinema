from django.db import models
# Create your models here.

class Horror_genre (models.Model):
    movie_name = models.CharField(max_length=50)
    dirctor_name = models.CharField(max_length=50)
    production_year = models.IntegerField()
    best_movie_actor = models.CharField(max_length=50)
    actorsbio = models.TextField()
    actorsimage = models.ImageField(default='', upload_to='actor_image/', null=True)
    actor_fav = models.BooleanField(default=True)
    def __str__(self):
        return self.movie_name


class Action(models.Model):
    movie_name = models.CharField(max_length=50)
    dir_name = models.CharField(max_length=50)
    prod_year = models.IntegerField()
    best_movie_actor = models.CharField(max_length=50)
    act_bio = models.TextField()
    actor_fav = models.BooleanField(default=True)
    def __str__(self):
        return self.movie_name

