#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #response = render(request, 'antifu/home.html', context_dict)

	return HttpResponse("Suck my dick!")
