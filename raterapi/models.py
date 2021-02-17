from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=1023)
	designer = models.CharField(max_length=255)
	release_year = models.IntegerField()
	num_players = models.IntegerField()
	est_time = models.IntegerField()
	age = models.IntegerField()

class GameImages(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	image = models.ImageField()

class Category(models.Model):
	category = models.CharField(max_length=255)

class GameCategories(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

class GameReviews(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.CharField(max_length=1023)

class GameRatings(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.IntegerField()