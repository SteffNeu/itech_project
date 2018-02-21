from django.shortcuts import render
from django.http import HttpResponse
from antifu.models import Category
from antifu.forms import UserForm,UserProfileForm

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

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'registration/registration_form.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})