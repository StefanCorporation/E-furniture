from django.shortcuts import render
from goods.models import Categories


def index(request):
    all_categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': all_categories
        }

    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About',
        'content': 'About Us',
        'text_on_page': 'Some text about this another ecomerse project lol ;)'
    })