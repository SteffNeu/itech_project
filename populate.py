import os
from django.db import IntegrityError
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech_project.settings')

import django
django.setup()
from antifu.models import Category, Post, Comment, UserProfile, FAQ, PersonalHelp
from django.contrib.auth.models import User

def populate():
    faqs = {"How do I censor my posts properly?":"Put a black block over everything that gives a clue to the identity of the original poster. i.e. name, profile pictures, names mentioned in the post",
            "How does the rating of the posts go?":"GrammarFail: how bad is the grammar of the post?" + os.linesep +
                                                   "LogicFail: how off is the post about the topic it is ranting about?" + os.linesep +
                                                   "Toxicity: how toxic do you think content like this is on the internet? Can this make more hate spread in the internet and provoke other people to hate." + os.linesep +
                                                   "Harmful: How harmful can this hateful post be to the people it is directed at. How personally attacked are the victims of the post." + os.linesep +
                                                   "Feeling: Did this comment affect you personally and made you feel a certain way? Let us and the rest of the community know. Maybe the original poster will see and realize what hurtful things he put out into the world and change his ways.   The higher you go on the scale, the higher you rate those categories." + os.linesep,
            "How does the rating of the comments work?":"Loveliness: Do you think the person was kind in their answer and deserves to be rewarded with a point of loveliness? "
                                                        "BurnFactor: Did the person manage to fire back (in a friendly manner) and completely debunk the original post with one simple and clear burn? Logic: Did the person manage to completely debunk the original post by applying pure, genius logic and showed the original post how wrong he was in his hate? "
                                                        "Accuracy: Did the person manage to debunk the original hate post on point? ",
            "How do I report an inappropriate post or comment?":"At the upper right side of comments and posts you can find a menu button that extends to show “edit” and “report”. If you want to report an inappropriate post or comment just click on it and choose a reason. ",
            "What is an inappropriate comment?":"Here on Anti-FU we aim to decrease hateful and hurtful content on the internet. Should you see any comments that themselves classify as hateful or hurtful because they are attacking, "
                                                "victimizing or insulting other individuals or groups that is an inappropriate comment. Help us keep this website kind and friendly and report that comment",
            "What is an inappropriate post? ":"A post can be inappropriate for several reasons. If the description is harmful or hurtful toward the posted picture. If the picture included in the post is not properly censored "
                                              "and gives away the identity of the original poster. Here at Anti-FU we do not want to additionally provoke people to express hatred and anger towards individuals. We don’t know why "
                                              "those people posted the things they posted and if we might misunderstand it. For that reason we aim to respect the privacy and identity of the original poster and rather encourage to "
                                              "kindly change people’s mind"}

    helps = {"Category: Cyber Bullying ":"",
             "What is Cyberbully exactly?":"http://www.stopcyberbullying.org/what_is_cyberbullying_exactly.html",
             "What is cyber bullying?":"https://www.bullying.co.uk/cyberbullying/what-is-cyberbullying/",
             "What is cyber bullying":"https://www.kidscape.org.uk/cyberbullying/",
             "Category: Prevention":"",
             "Effective Cyberbullying Prevention Strategies ":"http://www.cyberbullyhotline.com/blog/effective-cyberbullying-prevention-strategies/",
             "Preventing cyberbullying":"http://www.stopcyberbullying.org/prevention/index.htm",
             "Category: Intervention":"",
             "Take a stand against cyberbullying":"http://www.stopcyberbullying.org/take_action/take_a_stand_against_cyberbullying.html ",
             "Intervene in Cyberbullying":"http://preventingbullying.promoteprevent.org/cyberbullying/intervene-cyberbullying",
             "School-Based Cyberbullying Intervention":"https://gb.education.com/reference/article/school-based-cyberbullying-interventions/",
             "Cyberbullying: Resources for Intervention and Prevention ":"https://files.eric.ed.gov/fulltext/EJ1053892.pdf",
             "Interventions on Bullying and Cyberbullying in Schools: A Systematic Review": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4378064/",
             "Category: Getting Help": "",
             "HELP US, HELP YOU, STOP BULLYING": "http://www.nationalbullyinghelpline.co.uk/",
             "What to do if you’re being bullied on a social network ": "https://www.bullying.co.uk/cyberbullying/what-to-do-if-you-re-being-bullied-on-a-social-network/ ",
             "Bullying UK ": "http://ht.ly/ryD730gACeb",
             "Know your rights: Report, complain, campaign ":"http://www.stoponlineabuse.org.uk/",
             "Category: Suicide Prevention ":"",
             "Papyrus: prevention of young suicide ": "https://www.papyrus-uk.org/",
             "National Suicide Prevention Alliance": "https://www.samaritans.org/about-us/our-organisation/national-suicide-prevention-alliance-nspa ",
             "The Alliance of Suicide Prevention Charitie": "http://tasc-uk.org/"}
    users = [
        {
            "username":"TomCat",
            "email":"user@email.com",
            "password":"mypassw0rd",
            "picture":"profile_images/Scannen0002.jpg"

        },
        {
            "username": "PussCat",
            "email": "user2@email.com",
            "password": "newPassw0rd",
            "picture": "profile_images/pussCatImg.jpg"

        }
    ]

    comment = [
        {
            "comment": "It's called Bi-ble and not Straight-ble.",
            "date":"2007-05-10",
            "loveliness": 5,
            "burnfactor": 4,
            "logicRating": 2,
            "accuracyRating": 3
        },
        {
            "comment": "he IS perfect",
            "date":"2015-07-22",
            "loveliness": 78,
            "burnfactor": 0,
            "logicRating": 7,
            "accuracyRating": 20
        },
        {
            "comment": "you are just jealous",
            "date":"2015-07-25",
            "loveliness": 3,
            "burnfactor": 2,
            "logicRating": 9,
            "accuracyRating": 90
        }
    ]

    lgbtq_post = [
        {"title": "Adam and Steve",
         "context": "in tweeter",
         "tags": "#tag1 #tag2",
         "user": "",
         "date": "2007-05-10",
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
         "date": "2015-07-22",
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
            "LGBTQ": {"posts": lgbtq_post},
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
                post = add_post(c, p["title"], p["context"], user,p["date"], p["tags"],p["grammarFail"],
                            p["logicFail"],p["toxicity"],p["harmful"],p["report"],
                            p["views"],p["picturePost"]
                         )
                add_comm(post,comment[1],user2)
                add_comm(post,comment[2],user)

            elif cat_data["posts"] == lgbtq_post:
                post = add_post(c, p["title"], p["context"], user2,p["date"], p["tags"], p["grammarFail"],
                         p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                         p["views"], p["picturePost"])
                add_comm(post, comment[0], user)

    for q,value in faqs.items():
        add_faq(q,value)

    for h,value in helps.items():
        add_help(h,value)

#Creating superusers
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

#Adding categories
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

#Adding posts
def add_post(cat, title, context, user, date, tags, grammarFail,
            logicFail, toxicity, harmful, report, views, picturePost):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.context=context
    p.tags=tags
    p.user=user
    p.date=date
    p.grammarFail=grammarFail
    p.logicFail=logicFail
    p.toxicity=toxicity
    p.harmful=harmful
    p.report=report
    p.views=views
    p.picturePost=picturePost


    p.save()
    return p

#Adding comments
def add_comm(post,comment,user):
    comm = Comment.objects.get_or_create(comment=comment['comment'])[0]
    comm.burnfactor=comment["burnfactor"]
    comm.loveliness=comment['loveliness']
    comm.logicRating = comment['logicRating']
    comm.accuracyRating = comment['accuracyRating']
    comm.date=comment['date']
    comm.post=post
    comm.user=user

    comm.save()

#FAQS
def add_faq(q,a):
    FAQ.objects.get_or_create(questions=q,answers=a)

#PersonalHelp
def add_help(h,value):
    PersonalHelp.objects.get_or_create(title=h,href=value)

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
