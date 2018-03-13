from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from antifu.models import Category, UserProfile, Comment, Post
from antifu.forms import UserProfileForm, ContactForm, CommentForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError

from antifu.webhose_search import run_query

from datetime import datetime

# Create your views here.
def home(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render(request, 'antifu/home.html', context_dict)
    return render(request, 'antifu/home.html', context_dict)


def show_category(request, category_name):

    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category)
    comments = Comment.objects.filter(post=posts);
    if request.method =='GET':
        form = CommentForm()
    else:
        form = ContactForm(request.POST)
        comment = form.save(commit=False)
        comment.accuracyRating = 0
        comment.burnfactor = 0
        comment.logicRating = 0
        comment.loveliness = 0
        comment.comment = form.cleaned_data['comment']
        comment.save()


    context_dict = {'category':category,'posts':posts,'comments':comments, 'form':form}
    return render(request,'antifu/category.html',context_dict)


def aboutUs(request):
    return render(request, 'antifu/aboutUs.html')

def contactUs(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['2351944n@student.gla.ac.uk']
            if cc_myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, from_email, recipients)
            except BadHeaderError:
                return render(request, 'antifu/contactUs.html')
            context_dict = {'thanks': "true"}
            return render(request,'antifu/contactUs.html',context_dict)
         # if a GET (or any other method) we'll create a blank form
        else:
            form = ContactForm()
    return render(request, 'antifu/contactUs.html', {'form': form})

def personalHelp(request):
    return render(request, 'antifu/personalHelp.html')

def faq(request):
    return render(request, 'antifu/FAQ.html')

def post(request):

    post = Post.objects.all()
    comments = Comment.objects.all();
    context_dict = {'comments': comments, 'posts':post}
    return render(request, 'antifu/post.html', context_dict)

def comment(request):
    return render(request,'antifu/comment.html')


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('index')
        else:
            print(form.errors)
    context_dict = {'form':form}
    return render(request, 'registration/profile_registration.html', context_dict)


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

    return render(request, 'profile/profile.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form})

def myContents(request):
    return render(request, 'profile/MyContentsTab.html', {})

def search(request):
    result_list = []
    context_dict = {}
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Webhose search function to get the results list!
            result_list = run_query(query)
        context_dict['query'] = query
        context_dict['result_list'] = result_list
    return render(request, 'antifu/search.html', context_dict)
