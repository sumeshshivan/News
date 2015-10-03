from django.shortcuts import render
from models import NewsFeed, Category
# Create your views here.

def home(request):
	category_list = Category.objects.all()
	latest_news_list = NewsFeed.objects.all().order_by('-date_added')[:5]
	context = {'latest_news_list': latest_news_list, 'category_list': category_list}

	return render(request,'newsfeeds/home.html', context)

def category(request, category_id):
	try:
		category = Category.objects.get(pk=category_id)
		news_list = NewsFeed.objects.filter(category=category)
	except Category.DoesNotExist:
		raise Http404
	return render(request, 'newsfeeds/category.html', {'category': category, 'news_list': news_list})

def details(request, newsfeed_id):
	try:
		newsfeed = NewsFeed.objects.get(pk=newsfeed_id)
	except NewsFeed.DoesNotExist:
		raise Http404
	return render(request, 'newsfeeds/details.html', {'newsfeed': newsfeed})
