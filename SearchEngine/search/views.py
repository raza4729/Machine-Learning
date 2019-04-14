from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import gzip
import wikipedia
from search.forms import HomeForm

# Create your views here.

def index(request):
    if request.method == 'GET':
        trends_input_form = HomeForm(request.GET)
        inputstring = request.GET.get('post')
        print("------------------", str(inputstring))
        data = wikipedia.summary("google")
        my_dict = {'insert_me': data}
        return render(request, "search/index.html", context = my_dict)
    else:
        my_dict = {'inser': 'Hello'}
        return render(request,'search/index.html', context=my_dict)
