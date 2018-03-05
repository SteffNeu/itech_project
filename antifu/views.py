from django.shortcuts import render
from django.http import HttpResponse
from antifu.models import Category, UserProfile
from antifu.forms import UserProfileForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def home(request):
    # this is just an example for integration
    #category_list = Category.objects.order_by('-likes')[:5]
    #context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render(request, 'antifu/home.html', context_dict)
    return render(request, 'antifu/home.html',)

def show_category(request, category_name_slug):
    return HttpResponse("yeah bish")

def aboutUs(request):
    return render(request, 'antifu/aboutUs.html')

def contactUs(request):
    return render(request, 'antifu/contactUs.html')

def personalHelp(request):
    return render(request, 'antifu/personalHelp.html')

def faq(request):
    return render(request, 'antifu/FAQ.html')

@login_required
def register_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/antifu/')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=True)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm()

    return render(request, 'registration/profile_registration.html',
                  {'profile_form': profile_form})

@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/antifu/')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'antifu/profile.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form})
