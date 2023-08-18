import json
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from MainApp.models import Country, Language


def home(request):

    information_to_return = {
        'title': 'DjangoCountries',
        "privetstvie": "Hello everyone, this is my djangoproject",
    }

    return render(request, "home.html", information_to_return)


def get_country(request,name):

    country = Country.objects.get( country = name )
    information_to_return = {
        'title': country.country,
        'country': country.country,
        'languages': country.languages.all(),
    }

    return render(request, 'country.html', information_to_return)


def get_language(request,name):

    language = Language.objects.get( name = name )
    information_to_return = {
        'title': language.name,
        'language': language.name,
        'countries': Country.objects.filter(languages = language),
    }

    return render(request, 'language.html', information_to_return)


def get_countries_list(request):

    countries = Country.objects.all()
    letter = request.GET.get("letter")
    if letter:
        countries = countries.filter(country__startswith = letter)

    page = request.GET.get("page")
    if not page:
        page = 1
    try:
        page = int(page)
    except:
        page = 1   
    
    paginator = Paginator(countries, per_page = 10)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page)

    if paginator.num_pages >= page:
        information_to_return = {
            'title': 'Countries',
            "page": page,
            "letter": letter,
            "page_obj": page_obj,
            "alfabet": ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
        }
        return render(request, "countries_list.html", information_to_return)
    else:
        return HttpResponseNotFound(f"Page with number = {page} not found")


def get_languages_list(request):

    information_to_return = {
        'title': 'Languages',
        "languages_list": Language.objects.all(),
    }
    
    return render(request, "languages_list.html", information_to_return)