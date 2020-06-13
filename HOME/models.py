from django.db import models
from django.conf import settings
import datetime

class User(models.Model):
	user_name = models.CharField(max_length=50);
	user_mail = models.EmailField(max_length=254);
	user_pass = models.CharField(max_length=100);
	user_img = models.ImageField(upload_to = 'images/',default = 'images/default.jpg');
	user_best_score = models.FloatField(default=0);
	user_best_time = models.IntegerField(default=0);

	def __str__(self):
		return self.user_name

class Score(models.Model):
	user = models.ForeignKey('User',on_delete=models.CASCADE);
	time = models.IntegerField();
	score = models.FloatField();
	date =  models.DateTimeField(auto_now=True);
