from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=50)
	image = models.ImageField(blank=True)
	description = models.CharField('description', max_length=100,blank=True, help_text='simple description')
	create_date = models.DateTimeField('create_date', auto_now_add=True, blank=True, null=True)
	modify_date = models.DateTimeField('modify_date', auto_now=True, blank=True, null= True)

	def __str__(self):
		return self.title

