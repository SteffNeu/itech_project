from django.shortcuts import render
from django.http import HttpResponse
from antifu.models import Category

# Create your views here.
def home(request):
    # this is just an example for integration
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'antifu/home.html', context_dict)

def show_category(request, category_name_slug):
    return HttpResponse("yeah bish")

def aboutUs(request):
    return HttpResponse("yeah bish")

def personalHelp(request):
    return HttpResponse("yeah bish")
