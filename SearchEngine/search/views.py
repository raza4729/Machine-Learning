from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import gzip
import wikipedia
from search.forms import HomeForm

# Create your views here.

def searchmeth(request, query = None):

    if request.method == 'POST':
        name = request.POST.get('input_text', '')
    #     trends_input_form = HomeForm.objects.get(query=query)
    #     inputstring = request.GET.get('post')
    #     print('--------------', inputstring)
        data = wikipedia.summary(name)
        my_dict = {'insert_me': data}
        return render(request, "search/index.html", context = my_dict)
    else:
        return HttpResponse('Sorry!')

def index(request):
    my_dict = {'insert_in': ''}
    return render(request, 'search/index.html', context=my_dict)
