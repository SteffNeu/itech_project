import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech_project.settings')

import django
django.setup()
from antifu.models import Category, Post, Comment

def populate():

    comment = {"comment": "BOOOO",
                "loveliness": 5,
                "burnfactor": 4,
                "logicRating": 2,
                "accuracyRating": 3 }

    lgbtq_post = [
        {"title": "Adam and Steve",
        "context": "in tweeter",
        "tags": "#homophobic #lgbtq+",
        "grammarFail": 5,
        "logicFail": 46,
        "toxicity": 87,
        "harmful": 76,
        "report": 5,
        "views": 23,
        "picturePost": "post_pictures/Adam_And_Steve.PNG",
        "comment": {"comment1": comment}},
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


    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["posts"]:
            add_post(c, p["title"], p["context"],p["tags"],p["grammarFail"],
                        p["logicFail"],p["toxicity"],p["harmful"],p["report"],
                        p["views"],p["picturePost"],p["comment"])


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_post(cat, title, context, tags, grammarFail,
            logicFail, toxicity, harmful, report, views, picturePost, comment):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.context=context
    p.tags=tags
    p.grammarFail=grammarFail
    p.logicFail=logicFail
    p.toxicity=toxicity
    p.harmful=harmful
    p.report=report
    p.views=views
    p.picturePost=picturePost
    #comm=add_comm(comment)
    #p.comment=comm
    p.save()
    return p

def add_comm(post,comment):
    comm = Comment.objects.get_or_create(comment=comment)
    comm.comment=comment["comment"]
    comm.loveliness=comment.loveliness
# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
