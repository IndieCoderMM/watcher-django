from django.db import models
import uuid

class Character(models.Model):
	name = models.CharField(max_length=200)
	identity = models.CharField(max_length=200)
	origin = models.CharField(max_length=300)
	story = models.TextField(null=True)
	image = models.ImageField(upload_to='characters', blank=True,null=True)
	height = models.FloatField(null=True)
	intelligence = models.IntegerField(null=True)
	combat = models.IntegerField(null=True)
	strength = models.IntegerField(null=True)
	power = models.CharField(max_length=100)
	team = models.CharField(max_length=100)
	uuid = models.UUIDField(default=uuid.uuid4, unique=True)

	def __str__(self):
		return f"{self.name} [{self.identity}]"

