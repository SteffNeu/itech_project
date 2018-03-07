import os
from django.db import IntegrityError
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech_project.settings')

import django
django.setup()
from antifu.models import Category, Post, Comment, UserProfile
from django.contrib.auth.models import User

def populate():

    username = "TomCat"
    email = "user@email.com"
    password="mypassw0rd"
    picture = "H:\Internet-Technology\itech_project\static\images\Scannen0002.jpg"

    comment = {"comment": "YOLO",
                "loveliness": 5,
                "burnfactor": 4,
                "logicRating": 2,
                "accuracyRating": 3 }

    lgbtq_post = [
        {"title": "Adam and Steve",
        "context": "in tweeter",
        "tags": "#homophobic #lgbtq+",
        "user": "",
        "grammarFail": 5,
        "logicFail": 46,
        "toxicity": 87,
        "harmful": 76,
        "report": 5,
        "views": 23,
        "picturePost": "post_pictures/Adam_And_Steve.PNG",
        "comment": comment},
    ]

    cats = {"People": {"posts": lgbtq_post},
            "Racism": {"posts": lgbtq_post},
            "LGBTQ+": {"posts": lgbtq_post},
            "Politics": {"posts": lgbtq_post},
            "Troll": {"posts": lgbtq_post},
            "PassiveAggressive": {"posts": lgbtq_post},
            "Missinformation": {"posts": lgbtq_post},
            "Ableism": {"posts": lgbtq_post},
            "SelfHate": {"posts": lgbtq_post},
            "Relationships": {"posts": lgbtq_post},
            "Religious": {"posts": lgbtq_post}}


    user = create_su(username,email,password,picture)

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["posts"]:
            add_post(c, p["title"], p["context"], user, p["tags"],p["grammarFail"],
                        p["logicFail"],p["toxicity"],p["harmful"],p["report"],
                        p["views"],p["picturePost"],p["comment"])


def create_su(username, email, password, picture):
    try:
        u = User.objects.create_superuser(username, email, password)
        user = UserProfile.objects.get_or_create(user=u)[0]
        user.picture=picture
        user.save()
        u.save()
        return user
    except IntegrityError:
        pass


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_post(cat, title, context, user, tags, grammarFail,
            logicFail, toxicity, harmful, report, views, picturePost, comment):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.context=context
    p.tags=tags
    p.user=user
    p.grammarFail=grammarFail
    p.logicFail=logicFail
    p.toxicity=toxicity
    p.harmful=harmful
    p.report=report
    p.views=views
    p.picturePost=picturePost

    add_comm(p,comment,user)
    p.save()
    return p


def add_comm(post,comment,user):
    comm = Comment.objects.get_or_create(comment=comment['comment'])[0]
    comm.burnfactor=comment["burnfactor"]
    comm.loveliness=comment['loveliness']
    comm.logicRating = comment['logicRating']
    comm.accuracyRating = comment['accuracyRating']
    comm.post=post
    comm.user=user

    comm.save()

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()