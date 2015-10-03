from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('newsfeeds.views',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^newsfeed/(?P<newsfeed_id>\d+)/$', views.details, name='details'),
)