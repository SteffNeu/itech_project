from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from antifu.models import Category, UserProfile, Comment, Post, PersonalHelp, FAQ
from antifu.forms import UserProfileForm, ContactForm, uploadPostForm, UserForm

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse

from itertools import chain

from datetime import datetime

# Create your views here.
@csrf_protect
@csrf_exempt
def home(request):
    posts = Post.objects.order_by('-date')[:5]
    comments = Comment.objects.all()
    context_dict = {'posts':posts, 'comments':comments}
    result_list = []
    if request.method == 'POST':
        if 'query' in request.POST:
            query = request.POST['query'].strip()
            title_list = Post.objects.filter(title__contains=query)
            context_list = (Post.objects.filter(context__contains=query))
            value_list = list(chain(title_list, context_list))
            result_list = remove_duplicates(value_list)
            context_dict['query'] = query
            context_dict['result_list'] = result_list
            return render(request, 'antifu/search.html', context_dict)
    return render(request, 'antifu/home.html', context_dict)

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

@csrf_protect
@csrf_exempt
def show_category(request, category_name):
    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category)
    comments = Comment.objects.all()
    context_dict = {'category':category,'posts':posts,'comments':comments}


    return render(request,'antifu/category.html',context_dict)

@csrf_protect
@csrf_exempt
def show_post(request, post_id):
    selected_post = Post.objects.filter(id=post_id)
    comments = Comment.objects.all()
    context_dict = {'posts': selected_post, 'comments': comments}
    return render(request,'antifu/show_post.html',context_dict)

def aboutUs(request):
    context_dict = {}
    return render(request, 'antifu/aboutUs.html',context_dict)

@csrf_protect
@csrf_exempt
def contactUs(request):
    context_dict = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print (form)
            print ("happened")
            form.save(commit=True)
            context_dict = {'thanks': "true"}
            return render(request,'antifu/contactUs.html',context_dict)
         # if a GET (or any other method) we'll create a blank form
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'antifu/contactUs.html', {'form': form})


def personalHelp(request):
    help_obj = PersonalHelp.objects.all()

    cb_list = []
    prev_list = []
    interv_list = []
    help_list = []
    suiPrev_list = []

    for e in help_obj:
        if e.cbTitle is not '':
            cb_list.append({e.cbTitle:e.cbHref})
        if e.preventionTitle is not '':
            prev_list.append({e.preventionTitle:e.preventionHref})
        if e.interventionTitle is not '':
            interv_list.append({e.interventionTitle:e.interventionHref})
        if e.helpTitle is not '':
            help_list.append({e.helpTitle:e.helpHref})
        if e.suiPrevTitle is not '':
            suiPrev_list.append({e.suiPrevTitle:e.suiPrevHref})

    context_dict = {"help":help_list,
                    "cb":cb_list,
                    "prev":prev_list,
                    "interv":interv_list,
                    "sui":suiPrev_list,}
    return render(request, 'antifu/personalHelp.html',context_dict)


def faq(request):
    faqs = FAQ.objects.all()
    context_dict = {"faqs": faqs}
    return render(request, 'antifu/FAQ.html',context_dict)



def post(request, postID):
    post = Post.objects.get(id=postID)
    comments = Comment.objects.filter(post=post)
    context_dict = {'comments': comments, 'post':post}
    return render(request, 'antifu/post.html', context_dict)


@csrf_protect
@csrf_exempt
def submit_comment(request):
    if request.method == 'POST':

        #get the data
        data = request.POST

        #extract information
        post_id = data['post_id']
        username = data['user']
        comment = data['comment']

        #get user profile
        user = User.objects.get(username=username)
        try:
            userProfile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            userProfile = UserProfile.objects.create(user=user)

        print(userProfile)
        post = Post.objects.get(id=post_id)
        new_comment = Comment.objects.create(post=post,user=userProfile, comment=comment)
        new_comment.save()

        return render(request, 'antifu/comment.html', {'comment': new_comment})


@csrf_protect
@csrf_exempt
@login_required
def register_profile(request):
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
    context_dict = {'form':form}
    return render(request, 'registration/profile_registration.html', context_dict)


def calc_total_love(userprofile):
    comments = Comment.objects.filter(user=userprofile)

    love = 0
    for c in comments:
        love = c.loveliness + love
    return love


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/antifu/')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})

    userprofile.totallove = calc_total_love(userprofile)

    return render(request, 'profile/profile.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form,'profile_url':'/media/'})

@csrf_protect
@csrf_exempt
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
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)

    post_list = []

    #Posts the user made
    try:
        #filter works better than get, we can get multiple objects
        post_list = Post.objects.filter(user=userprofile)
    except Post.DoesNotExist:
        print('no posts')

    numComments = []

    #Comments of each post
    try:
        for p in post_list:
            post_comment_list = Comment.objects.filter(post=p)
            numComments.append({p: len(post_comment_list)})
    except Comment.DoesNotExist:
        print('no comments')

    context_dict = {"numComments": numComments, }
    return render(request, 'profile/MyContentsTab.html', context_dict)


def myComments(request, username):
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    user_comment_list=[]

    #Comments the user made
    try:
        user_comment_list = Comment.objects.filter(user=userprofile)
    except Comment.DoesNotExist:
        print('no comments')

    context_dict={"comments":user_comment_list}
    return render(request, 'profile/MyCommentsTab.html', context_dict)

@csrf_protect
@csrf_exempt
def settings(request):
    userprofile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm({'picture': userprofile.picture})

    if request.method=='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        user = request.user
        user.first_name = request.POST.get('fname', '')
        user.last_name = request.POST.get('lname', '')
        user.email = request.POST.get('email', '')
        new_name = request.POST.get('username', '')

        if not User.objects.filter(username=new_name).exists():
            user.username = request.POST.get('username', '')
        user.save()

        if form.is_valid():
            userprofile.user.first_name = request.POST.get('fname', '')
            userprofile.save()
            form.save(commit=True)
        else:
            print('NOT VALID')
        return render(request, 'profile/redirect_template.html', {'selecteduser':request.user})
    return render(request, 'profile/MySettingsTab.html', {'form':form,
                                                          'selecteduser':request.user})

@csrf_protect
@csrf_exempt
def uploadContent(request):
    form=uploadPostForm()
    if request.method== 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST.get('category',''))
            userProfile = UserProfile.objects.get(user=request.user)
            category = Category.objects.get(name=request.POST.get('category',''))
            post = Post.objects.create(category=category,user=userProfile,title=request.POST.get('title',''),context=request.POST.get('context',''),picturePost=request.FILES.get('pic',''))
            form = UserProfileForm(instance=post)
            post = form.save(commit=False)
            post.save()
        return render(request, 'profile/redirect_template.html', {'selecteduser': request.user})
    return render(request, 'profile/UploadContentTab.html', {'form':form})


@csrf_protect
@csrf_exempt
def update_comment_feat(request):

    if request.method == 'POST':
        data = request.POST
        comment_id = data['comment_id']
        value = data['value']
        feat = data['feat']

        comment = Comment.objects.get(id=comment_id)

        if feat == "loveliness":
            comment.loveliness = value
        elif feat == "burnfactor":
            comment.burnfactor = value
        elif feat == "logicRating":
            comment.logicRating = value
        else:
            comment.accuracyRating = value

        comment.save()

    return HttpResponse(" ")

@csrf_protect
@csrf_exempt
def update_post_feat(request):

    if request.method == 'POST':
        data = request.POST
        post_id = data['post_id']
        value = data['value']
        feat = data['feat']

        post = Post.objects.get(id=post_id)

        if feat == "logicFail":
            post.logicFail = value
        elif feat == "grammarFail":
            post.grammarFail = value
        elif feat == "harmful":
            post.harmful = value
        elif feat == "toxicity":
            post.toxicity = value

        post.save()

    return HttpResponse(" ")

@csrf_protect
@csrf_exempt
def report(request):

    if request.method == 'POST':
        data = request.POST
        id = data['id']
        flag = data['flag']

        if flag == "post":
            post = Post.objects.get(id=id)
            post.report = post.report+1
            print(post.report)

            post.save()
        else:
            comment = Comment.objects.get(id=id)
            comment.report = comment.report + 1
            comment.save()

    return HttpResponse("")

@csrf_protect
@csrf_exempt
def update_comment_content(request):

    if request.method == 'POST':
        data = request.POST
        comment_id = data['comment_id']
        new_comment = data['comment_content']

        comment = Comment.objects.get(id=comment_id)
        comment.comment = new_comment
        comment.save()
    return HttpResponse(" ")


def del_user(request):
    try:
        u = User.objects.get(username=request.user)
        u.delete()

    except User.DoesNotExist:
        print('does not exist')
        return render(request, 'profile/redirect_template.html', {'selecteduser': request.user})

    except Exception as e:
        print('error')
        return render(request, 'profile/redirect_template.html', {'selecteduser': request.user})

    return render(request, 'profile/redirect_template.html', {'selecteduser': request.user})