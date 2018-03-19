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






    helpLinks = [
        # helpLinks[0] - Cyber bullying
        {
             "What is Cyberbully exactly?":"http://www.stopcyberbullying.org/what_is_cyberbullying_exactly.html",
             "What is cyber bullying?":"https://www.bullying.co.uk/cyberbullying/what-is-cyberbullying/",
             "What is cyber bullying":"https://www.kidscape.org.uk/cyberbullying/"},
        # helpLinks[1] - Prevention
        {
            "Effective Cyberbullying Prevention Strategies ":"http://www.cyberbullyhotline.com/blog/effective-cyberbullying-prevention-strategies/",
             "Preventing cyberbullying":"http://www.stopcyberbullying.org/prevention/index.html"},
        # helpLinks[2] - Intervention
        {     "Take a stand against cyberbullying":"http://www.stopcyberbullying.org/take_action/take_a_stand_against_cyberbullying.html ",
             "Intervene in Cyberbullying":"http://preventingbullying.promoteprevent.org/cyberbullying/intervene-cyberbullying",
             "School-Based Cyberbullying Intervention":"https://gb.education.com/reference/article/school-based-cyberbullying-interventions/",
             "Cyberbullying: Resources for Intervention and Prevention ":"https://files.eric.ed.gov/fulltext/EJ1053892.pdf",
             "Interventions on Bullying and Cyberbullying in Schools: A Systematic Review": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4378064/"},
        # helpLinks[3] - Getting help
        {
             "HELP US, HELP YOU, STOP BULLYING": "http://www.nationalbullyinghelpline.co.uk/",
             "What to do if you are being bullied on a social network ": "https://www.bullying.co.uk/cyberbullying/what-to-do-if-you-re-being-bullied-on-a-social-network/ ",
             "Bullying UK ": "http://ht.ly/ryD730gACeb",
             "Know your rights: Report, complain, campaign ":"http://www.stoponlineabuse.org.uk/"},
        # helpLinks[4] - Suicide prevention
        {
             "Papyrus: prevention of young suicide ": "https://www.papyrus-uk.org/",
             "National Suicide Prevention Alliance": "https://www.samaritans.org/about-us/our-organisation/national-suicide-prevention-alliance-nspa ",
             "The Alliance of Suicide Prevention Charity": "http://tasc-uk.org/"}]

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
         "picturePost": "post_pictures/ryangosling.jpg",
         },
    ]

    ableism_post = [
        {"title": "Handicap parking spot",
         "context": "taking up spaces designated for handicapped people",
         "user": "",
         "date": "2015-12-12",
         "grammarFail": 1,
         "logicFail": 100,
         "toxicity": 99,
         "harmful": 75,
         "report": 0,
         "views": 160,
         "picturePost": "post_pictures/ableist.jpg",
         },
    ]


    racism_post = [
        {"title": "AIDS in Africa?",
         "context": "misinformation from white privilege",
         "user": "",
         "date": "2014-01-01",
         "grammarFail": 1,
         "logicFail": 300,
         "toxicity": 231,
         "harmful": 100,
         "report": 0,
         "views": 370,
         "picturePost": "post_pictures/racistrace.jpg",
         },
    ]

    politics_post = [
        {"title": "Hillary Clinton",
         "context": "smear campaign misinformation",
         "user": "",
         "date": "2017-12-01",
         "grammarFail": 2,
         "logicFail": 300,
         "toxicity": 354,
         "harmful": 77,
         "report": 0,
         "views": 355,
         "picturePost": "post_pictures/politics.jpg",
         },
    ]

    troll_post = [
        {"title": "I Hate everything",
         "context": "person goes off hating everything for no apparent reason",
         "user": "",
         "date": "2016-09-09",
         "grammarFail": 5,
         "logicFail": 99,
         "toxicity": 229,
         "harmful": 189,
         "report": 0,
         "views": 255,
         "picturePost": "post_pictures/everything.jpg",
         },
    ]

    passiveAgressive_post = [
        {"title": "Just you wait, mom",
         "context": "friend does this when mad at their mom",
         "user": "",
         "date": "2018-02-09",
         "grammarFail": 1,
         "logicFail": 90,
         "toxicity": 209,
         "harmful": 181,
         "report": 0,
         "views": 155,
         "picturePost": "post_pictures/passiveAgressive.jpg",
         },
    ]

    missinformation_post = [
        {"title": "Thanks Obama",
         "context": "came across this little gem",
         "user": "",
         "date": "2017-04-13",
         "grammarFail": 90,
         "logicFail": 401,
         "toxicity": 20,
         "harmful": 20,
         "report": 0,
         "views": 555,
         "picturePost": "post_pictures/rascism_politics.jpg",
         },
    ]

    selfHate_post = [
        {"title": "Hate myself",
         "context": "a classmate said this while talking about mental issues",
         "user": "",
         "date": "2017-05-13",
         "grammarFail": 0,
         "logicFail": 101,
         "toxicity": 2,
         "harmful": 54,
         "report": 0,
         "views": 172,
         "picturePost": "post_pictures/selfhate.jpg",
         },
    ]

    relationship_post = [
        {"title": "Cheating",
         "context": "someone offering their opinion on cheating",
         "user": "",
         "date": "2017-05-13",
         "grammarFail": 1,
         "logicFail": 299,
         "toxicity": 399,
         "harmful": 399,
         "report": 0,
         "views": 400,
         "picturePost": "post_pictures/relationship.jpg",
         },
    ]

    religion_post = [
        {"title": "Muslim hate",
         "context": "in reaction to the muslim ban",
         "user": "",
         "date": "2017-02-11",
         "grammarFail": 5,
         "logicFail": 202,
         "toxicity": 299,
         "harmful": 297,
         "report": 0,
         "views": 305,
         "picturePost": "post_pictures/religion.jpg",
         },
    ]

    cats = {"People": {"posts": people_post},
            "Racism": {"posts":racism_post},
            "LGBTQ": {"posts": lgbtq_post},
            "Politics": {"posts": politics_post},
            "Troll": {"posts": troll_post},
            "PassiveAggressive": {"posts": passiveAgressive_post},
            "Missinformation": {"posts": missinformation_post},
            "Ableism": {"posts": ableism_post},
            "SelfHate": {"posts": selfHate_post},
            "Relationships": {"posts": relationship_post},
            "Religious": {"posts": religion_post}}


    user = create_su(users[0]["username"],users[0]["email"],users[0]["password"],users[0]["picture"])
    user2 = create_su(users[1]["username"], users[1]["email"], users[1]["password"], users[1]["picture"])

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["posts"]:
            if cat_data["posts"] == people_post:
                post = add_post(c, p["title"], p["context"], user,p["date"], p["grammarFail"],
                            p["logicFail"],p["toxicity"],p["harmful"],p["report"],
                            p["views"],p["picturePost"]
                         )
                add_comm(post,comment[1],user2)
                add_comm(post,comment[2],user)

            elif cat_data["posts"] == lgbtq_post:
                post = add_post(c, p["title"], p["context"], user2,p["date"], p["grammarFail"],
                         p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                         p["views"], p["picturePost"])
                add_comm(post, comment[0], user)

            elif cat_data["posts"] == racism_post:
                post = add_post(c, p["title"], p["context"], user, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == politics_post:
                post = add_post(c, p["title"], p["context"], user2, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == troll_post:
                post = add_post(c, p["title"], p["context"], user, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == passiveAgressive_post:
                post = add_post(c, p["title"], p["context"], user2, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == missinformation_post:
                post = add_post(c, p["title"], p["context"], user, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == ableism_post:
                post = add_post(c, p["title"], p["context"], user2, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == selfHate_post:
                post = add_post(c, p["title"], p["context"], user, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == relationship_post:
                post = add_post(c, p["title"], p["context"], user2, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])
            elif cat_data["posts"] == religion_post:
                post = add_post(c, p["title"], p["context"], user, p["date"], p["grammarFail"],
                                p["logicFail"], p["toxicity"], p["harmful"], p["report"],
                                p["views"], p["picturePost"])


    for q,value in faqs.items():
        add_faq(q,value)

    i = 0
    for h in helpLinks:
        i = i + 1
        for k,value in h.items():
            add_help(k,value,i)

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
def add_post(cat, title, context, user, date, grammarFail,
            logicFail, toxicity, harmful, report, views, picturePost):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.context=context
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
def add_help(h,value,i):
    if i==1:
        PersonalHelp.objects.get_or_create(cbTitle=h,cbHref=value)
    elif i==2:
        PersonalHelp.objects.get_or_create(preventionTitle=h, preventionHref=value)
    elif i==3:
        PersonalHelp.objects.get_or_create(interventionTitle=h, interventionHref=value)
    elif i==4:
        PersonalHelp.objects.get_or_create(helpTitle=h, helpHref=value)
    else:
        PersonalHelp.objects.get_or_create(suiPrevTitle=h, suiPrevHref=value)

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
