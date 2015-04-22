from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200)
	article = models.TextField(max_length = 15000)
	date = models.DateTimeField()


	def __unicode__(self):
		return self.title