from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
import wikipedia
import wikipediaapi
from search.forms import HomeForm

# Create your views here.

def searchmeth(request, query = None):

    if request.method == 'POST':
        name = request.POST.get('input_text', '')

        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(name)

        # print("Page - Title: %s" % page_py.title)
        # Page - Title: Python (programming language)
        # data = page_py.summary

        categories = page_py.categories
        for title in sorted(categories.keys()):
            print("%s: %s" % (title, categories[title]))
        # word_counter = {}
        # for word in categories:
        #     if word in word_counter:
        #         word_counter[word] += 1
        #     else:
        #         word_counter[word] = 1
        # popular_words = sorted(word_counter, key=word_counter.get, reverse=True)
        # top_3 = popular_words[:3]

        # print(len(categories))
        my_dict = {'insert_me': categories}
        return render(request, "search/index.html", context = my_dict)
    else:
        return HttpResponseRedirect('/index/')

def index(request):
    my_dict = {'insert_in': ''}
    return render(request, 'search/index.html', context=my_dict)
