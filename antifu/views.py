from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from antifu.models import Category, UserProfile, Comment, Post, PersonalHelp, FAQ
from antifu.forms import UserProfileForm, ContactForm, CommentForm

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
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
    category_list = Category.objects.all()
    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category)
    comments = Comment.objects.filter(post=posts);
    form = CommentForm();
    context_dict = {'category':category,'posts':posts,'comments':comments, 'form':form,'categories': category_list}

    return render(request,'antifu/category.html',context_dict)


def aboutUs(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'antifu/aboutUs.html',context_dict)

def contactUs(request):
    category_list = Category.objects.all()
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
    return render(request, 'antifu/contactUs.html', {'form': form,'categories': category_list})

def personalHelp(request):
    category_list = Category.objects.all()
    help_list = PersonalHelp.objects.all()
    context_dict = {"help":help_list,
                    'categories': category_list}
    return render(request, 'antifu/personalHelp.html',context_dict)

def faq(request):
    category_list = Category.objects.all()
    faqs = FAQ.objects.all()
    context_dict = {"faqs": faqs,
                    'categories': category_list}
    return render(request, 'antifu/FAQ.html',context_dict)

def post(request, postID):
    category_list = Category.objects.all()
    post = Post.objects.get(id=postID)
    comments = Comment.objects.filter(post=post);
    context_dict = {'comments': comments, 'post':post,'categories': category_list}
    return render(request, 'antifu/post.html', context_dict)

@csrf_protect
@csrf_exempt
def submit_comment(request):
    #user comment post_id
    post_id = 1
    user = User.objects.get(username="TomCat")
    userProfile = UserProfile.objects.get(user=user)
    print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
    if request.method == 'POST':
        print("I get the post")
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print("The form is valid")
            comment = form.cleaned_data['comment']
            print("my comment :" + comment)
            post = Post.objects.get(id=post_id)
            new_comment = Comment.objects.create(post=post,user=userProfile, comment=comment)
            new_comment.save()

            return new_comment


@login_required
def register_profile(request):
    category_list = Category.objects.all()
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect('home')
    else:
        print(form.errors)
    context_dict = {'form':form,'categories': category_list}
    return render(request, 'registration/profile_registration.html', context_dict)

@login_required
def profile(request, username):
    category_list = Category.objects.all()
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
        {'userprofile': userprofile, 'selecteduser': user, 'form': form,'profile_url':'/media/','categories': category_list})


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

#for the nav tabs
def myContents(request, username):
    user=User.objects.get(username=username)
    userprofile=UserProfile.objects.get(user=user)
    post_list=[]
    post_comment_list=[]

    #Posts the user made
    try:
        #filter works better than get, we can get multiple objects
        post_list = Post.objects.filter(user=userprofile)
    except Post.DoesNotExist:
        print('no posts')

    #Comments of each post
    try:
        for p in post_list:
            post_comment_list = Comment.objects.filter(post=p)
    except Comment.DoesNotExist:
        print('no comments')

    numComments = len(post_comment_list)
    context_dict={"posts":post_list,
                "numComments":numComments,
                "postComments":post_comment_list}
    return render(request, 'profile/MyContentsTab.html', context_dict)


def myComments(request, username):
    user=User.objects.get(username=username)
    userprofile=UserProfile.objects.get(user=user)
    user_comment_list=[]

    #Comments the user made
    try:
        user_comment_list = Comment.objects.filter(user=userprofile)
    except Comment.DoesNotExist:
        print('no comments')


    context_dict={"comments":user_comment_list}
    return render(request, 'profile/MyCommentsTab.html', context_dict)

def settings(request):
    return render(request, 'profile/MySettingsTab.html', {})

def uploadContent(request):
    return render(request, 'profile/UploadContentTab.html', {})
