from django import template
from antifu.models import Category, Comment, Post

register = template.Library()

@register.inclusion_tag('antifu/cats.html')
def get_category_list(cat = None):
    return {'cats': Category.objects.all(),
            'act_cat': cat}

# here we need one certain comment we should get via id
@register.inclusion_tag('antifu/comment.html')
def get_comment(commentID = None, user=None):
    return{'comment':Comment.objects.get(id = commentID),'user':user}

# here we need one certain post we should get via id
@register.inclusion_tag('antifu/post.html')
def get_post(postID = None):
    return{'post':Post.objects.get(id = postID)}

@register.inclusion_tag('antifu/post_comment_submit.html')
def get_post_comment_submit(posts, comments, user):
    return{'posts':posts,'comments':comments, 'user':user}

# here we need one certain comment rating we should get via the id of the comment we request the rating from
@register.inclusion_tag('antifu/comment_rating.html')
def get_comment_rating_list(commentID = None):
    return{}

# here we need one certain post rating we should get via the id of the post we request the rating from
@register.inclusion_tag('antifu/post_rating.html')
def get_post_rating(postID = None):
    return{}

# don't know what we need. since we submit data and not take from database
@register.inclusion_tag('antifu/post_comment_submit.html')
def get_complete_pcs_list():
    return{}
