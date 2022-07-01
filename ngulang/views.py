from django.shortcuts import render
from .models import Food, Ingredient, Book
from django.db.models import Count

# Create your views here.


def food_list(request):
    # get all
    foods = Food.objects.all()
    # filter
    food_filters = Food.objects.filter(name='nasi goreng').values()
    # get
    food_gets = Food.objects.get(name='nasi goreng')
    # first
    food_firsts = Food.objects.first()
    # aggregat
    aggregats = Food.objects.aggregate(Count('name'))
    # annotate
    annotates = Food.objects.annotate(Count('name'))
    # select related
    # https://zerotobyte.com/how-to-use-django-select-related-and-prefetch-related/
    selects = Ingredient.objects.select_related('food').all()
    select_calls = Ingredient.objects.select_related(
        'food').get(id=1).food.name
    # prefetch
    prefetchs = Book.objects.all().prefetch_related('authors')

    return render(request, 'ngulang/index.html',  {'foods': foods, 'food_filters': food_filters, 'food_firsts': food_firsts, 'food_gets': food_gets, 'aggregats': aggregats, 'annotates': annotates, 'selects': selects, 'select_calls': select_calls, 'prefetchs': prefetchs})
