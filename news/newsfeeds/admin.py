from django.contrib import admin
from newsfeeds.models import Category, NewsFeed

# Register your models here.

admin.site.register(Category)
admin.site.register(NewsFeed)