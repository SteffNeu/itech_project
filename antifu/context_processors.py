from antifu.models import Category

def categories(request):
    return{'categories': Category.objects.all()}

def search_request(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = Post.objects.filter(title__contains=query)
            return{'result_list': Post.objects.filter(title__contains=query)}
