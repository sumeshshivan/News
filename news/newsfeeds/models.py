from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.name

class NewsFeed(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey(Category)
	stared = models.BooleanField(default=False)
	story = models.TextField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
	photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title