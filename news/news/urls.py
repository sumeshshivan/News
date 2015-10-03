from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news.views.home', name='home'),
    url(r'^', include('newsfeeds.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )