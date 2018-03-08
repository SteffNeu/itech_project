import os
from django.db import IntegrityError
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech_project.settings')

import django
django.setup()
from antifu.models import Category, Post, Comment, UserProfile
from django.contrib.auth.models import User

def populate():

    users = [
        {
            "username":"TomCat",
            "email":"user@email.com",
            "password":"mypassw0rd",
            "picture":"Scannen0002.jpg"

        },
        {
            "username": "PussCat",
            "email": "user2@email.com",
            "password": "newPassw0rd",
            "picture": "pussCatImg.jpg"

        }
    ]

    comment = [
        {
            "comment": "YOLO",
            "loveliness": 5,
            "burnfactor": 4,
            "logicRating": 2,
            "accuracyRating": 3
        },
        {
            "comment": "he IS perfect",
            "loveliness": 78,
            "burnfactor": 0,
            "logicRating": 7,
            "accuracyRating": 20
        },
        {
            "comment": "you are just jealous",
            "loveliness": 3,
            "burnfactor": 2,
            "logicRating": 9,
            "accuracyRating": 90
        }
    ]

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
         "picturePost": "post_pictures/Adam_And_Steve.PNG"},
    ]

    people_post = [
        {"title": "Ryan Gosling",
         "context": "celebrities read mean tweets",
         "tags": "#theotherryan #not-deadpool #perfectcheekbone",
         "user": "",
         "grammarFail": 2,
         "logicFail": 100,
         "toxicity": 187,
         "harmful": 3,
         "report": 1,
         "views": 260,
         "picturePost": "post_pictures/ryan-gosling-tweets.jpg",
         },
    ]

    cats = {"People": {"posts": people_post},
            "Racism": {"posts": ""},
            "LGBTQ+": {"posts": lgbtq_post},
            "Politics": {"posts": ""},
            "Troll": {"posts": ""},
            "PassiveAggressive": {"posts": ""},
            "Missinformation": {"posts": ""},
            "Ableism": {"posts": ""},
            "SelfHate": {"posts": ""},
            "Relationships": {"posts": ""},
            "Religious": {"posts": ""}}


    user = create_su(users[0]["username"],users[0]["email"],users[0]["password"],users[0]["picture"])
    user2 = create_su(users[1]["username"], users[1]["email"], users[1]["password"], users[1]["picture"])

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["posts"]:
            if cat_data["posts"] == people_post:
                post = add_post(c, p["title"], p["context"], user, p["tags"],p["grammarFail"],
                            p["logicFail"],p["toxicity"],p["harmful"],p["report"],
                            p["views"],p["picturePost"]
                         )

                add_comm(post,comment[1],user2)
                add_comm(post,comment[2],user)
            elif cat_data["posts"] == lgbtq_post:
                post = add_post(c, p["title"], p["context"], user2, p["tags"], p["grammarFail"],
                         p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                         p["views"], p["picturePost"])
                add_comm(post, comment[0], user)


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
            logicFail, toxicity, harmful, report, views, picturePost):
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