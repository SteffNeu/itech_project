from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from antifu.models import Post,Comment,Category,UserProfile, ContactUsEmail, FAQ, PersonalHelp
from datetime import date

#####Tests for the model######
class PostModelTests(TestCase):

    def setUp(self):
        # create test category for reference
        self.cat = Category(name="testName")
        self.cat.save()

        #create test user
        self.user = User.objects.create_user("testUser", "test@email.com", "testPassword")
        self.user.save()

        #create profile for the user
        self.u_profile = UserProfile(user=self.user)
        self.u_profile.save()

    def test_ensure_grammarFail_is_positive(self):
        post = Post(category=self.cat,grammarFail=0)
        post.save()
        self.assertEqual((post.grammarFail >= 0), True)

    def test_ensure_logicFail_is_positive(self):
        post = Post(category=self.cat,logicFail=0)
        post.save()
        self.assertEqual((post.logicFail >= 0), True)

    def test_ensure_toxicity_is_positive(self):
        post = Post(category=self.cat,toxicity=0)
        post.save()
        self.assertEqual((post.toxicity >= 0), True)

    def test_ensure_harmful_is_positive(self):
        post = Post(category=self.cat,harmful=0)
        post.save()
        self.assertEqual((post.harmful >= 0), True)

    def test_ensure_report_is_positive(self):
        post = Post(category=self.cat,report=0)
        post.save()
        self.assertEqual((post.report >= 0), True)

    def test_ensure_correct_date_post(self):
        post = Post(category=self.cat)
        post.save()
        #get current date
        today = date.today()
        self.assertEqual((post.date == today), True)

    def test_ensure_id_increment_post(self):
        first_post = Post(category=self.cat)
        first_post.save()
        second_post = Post(category=self.cat)
        second_post.save()
        self.assertIs(1,second_post.id-first_post.id)

    def test_confirm_user_post(self):
        post = Post(category=self.cat,user=self.u_profile)
        post.save()
        self.assertIsNotNone(post.user)

    def test_confirm_title_of_post(self):
        testTitle = "Some title"
        post = Post(category=self.cat,title=testTitle)
        post.save()
        self.assertIsNotNone(post.title)

    def test_confirm_content_of_title(self):
        testTitle = "Some title"
        post = Post(category=self.cat,title=testTitle)
        post.save()
        self.assertEqual(testTitle,post.title)

    def test_confirm_context_of_post(self):
        testContext = "The context of the post"
        post = Post(category=self.cat,context=testContext)
        post.save()
        self.assertIsNotNone(post.context)

    def test_confirm_content_of_context(self):
        testContext = "The context of the post"
        post = Post(category=self.cat,context=testContext)
        post.save()
        self.assertEqual(testContext,post.context)


class CommentModelTests(TestCase):

    def setUp(self):
        # create test category for reference
        self.cat = Category(name="testName")
        self.cat.save()

        #create test user
        self.user = User.objects.create_user("testUser", "test@email.com", "testPassword")
        self.user.save()

        #create profile for the user
        self.u_profile = UserProfile(user=self.user)
        self.u_profile.save()

        #create test post
        self.post = Post(category=self.cat,user=self.u_profile)
        self.post.save()

    def test_ensure_id_increment_comment(self):
        first_comment = Comment(post=self.post,user=self.u_profile)
        first_comment.save()
        second_comment = Comment(post=self.post,user=self.u_profile)
        second_comment.save()
        self.assertIs(1,second_comment.id-first_comment.id)

    def test_ensure_loveliness_is_positive(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertEqual((comment.loveliness >= 0), True)

    def test_ensure_burnfactor_is_positive(self):
        comment = Comment(post=self.post,user=self.u_profile,burnfactor=0)
        comment.save()
        self.assertEqual((comment.burnfactor >= 0), True)

    def test_ensure_logicRating_is_positive(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertEqual((comment.logicRating >= 0), True)

    def test_ensure_accuracyRating_is_positive(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertEqual((comment.accuracyRating >= 0), True)

    def test_ensure_report_is_positive(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertEqual((comment.report >= 0), True)

    def test_ensure_correct_date_comment(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        #get current date
        today = date.today()
        self.assertEqual((comment.date == today), True)

    def test_confirm_comment_of_comment_exists(self):
        testComment = "This is a lovely comment"
        comment = Comment(post=self.post,user=self.u_profile,comment=testComment)
        comment.save()
        self.assertIsNotNone(comment.comment)

    def test_confirm_content_of_comment(self):
        testComment = "This is a lovely comment"
        comment = Comment(post=self.post,user=self.u_profile,comment=testComment)
        comment.save()
        self.assertEqual(testComment,comment.comment)

    def test_confirm_user_of_comment_exists(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertIsNotNone(comment.user)

    def test_confirm_user_of_comment(self):
        comment = Comment(post=self.post, user=self.u_profile)
        comment.save()
        self.assertEqual(self.u_profile, comment.user)

    def test_confirm_post_of_comment_exists(self):
        comment = Comment(post=self.post,user=self.u_profile)
        comment.save()
        self.assertIsNotNone(comment.post)

    def test_confirm_post_of_comment(self):
        comment = Comment(post=self.post, user=self.u_profile)
        comment.save()
        self.assertEqual(self.post, comment.post)

class ContactUsEmailTests(TestCase):

    def test_confirm_name_of_contactUs_exists(self):
        testName = "testName"
        contactUs = ContactUsEmail(name=testName)
        contactUs.save()
        self.assertIsNotNone(contactUs.name)

    def test_confirm_content_of_name(self):
        testName = "testName"
        contactUs = ContactUsEmail(name=testName)
        contactUs.save()
        self.assertEqual(testName,contactUs.name)

    def test_confirm_emai_of_contactUs_exists(self):
        testEmail = "test@email.com"
        contactUs = ContactUsEmail(from_email=testEmail)
        contactUs.save()
        self.assertIsNotNone(contactUs.from_email)

    def test_confirm_content_of_from_email(self):
        testEmail = "test@email.com"
        contactUs = ContactUsEmail(from_email=testEmail)
        contactUs.save()
        self.assertEqual(testEmail,contactUs.from_email)

    def test_confirm_subject_of_contactUs_exists(self):
        testSubject = "testSubject"
        contactUs = ContactUsEmail(subject=testSubject)
        contactUs.save()
        self.assertIsNotNone(contactUs.subject)

    def test_confirm_content_of_subject(self):
        testSubject = "testSubject"
        contactUs = ContactUsEmail(subject=testSubject)
        contactUs.save()
        self.assertEqual(testSubject,contactUs.subject)

    def test_confirm_message_of_contactUs_exists(self):
        testMessage = "test-message"
        contactUs = ContactUsEmail(message=testMessage)
        contactUs.save()
        self.assertIsNotNone(contactUs.message)

    def test_confirm_content_of_message(self):
        testMessage = "test-message"
        contactUs = ContactUsEmail(message=testMessage)
        contactUs.save()
        self.assertEqual(testMessage,contactUs.message)

class CategoryModelTests(TestCase):
    def test_confirm_name_of_category_exists(self):
        testCategory = "category-name"
        category = Category(name=testCategory)
        category.save()
        self.assertIsNotNone(category.name)

    def test_confirm_content_of_name(self):
        testCategory = "category-name"
        category = Category(name=testCategory)
        category.save()
        self.assertEqual(testCategory,category.name)

class UserProfileModelTests(TestCase):

    def setUp(self):
        #create test user
        self.user = User.objects.create_user("testUser", "test@email.com", "testPassword")
        self.user.save()

    def test_confirm_user_of_profile_exists(self):
        userprofile = UserProfile(user = self.user)
        userprofile.save()
        self.assertIsNotNone(userprofile.user)

    def test_confirm_content_of_user_of_userprofile(self):
        userprofile = UserProfile(user = self.user)
        userprofile.save()
        self.assertEqual(self.user,userprofile.user)

    def test_ensure_totallove_is_positive(self):
        userprofile = UserProfile(user = self.user,totallove=0)
        userprofile.save()
        self.assertEqual((userprofile.totallove >= 0), True)

class FAQModelTest(TestCase):
    def test_confirm_questios_of_FAQ_exists(self):
        testQuestion = "testQuest"
        faq = FAQ(questions=testQuestion)
        faq.save()
        self.assertIsNotNone(faq.questions)

    def test_confirm_content_of_questions(self):
        testQuestion = "testQuest"
        faq = FAQ(questions=testQuestion)
        faq.save()
        self.assertEqual(testQuestion,faq.questions)

    def test_confirm_answers_of_FAQ_exists(self):
        testAnswer = "testAnswer"
        faq = FAQ(answers=testAnswer)
        faq.save()
        self.assertIsNotNone(faq.answers)

    def test_confirm_content_of_answers(self):
        testAnswers = "testanswer"
        faq = FAQ(answers=testAnswers)
        faq.save()
        self.assertEqual(testAnswers,faq.answers)

class PersonalHelpModelTest(TestCase):

    def test_confirm_cbTitle_of_personalHelp_exists(self):
        testTitle = "testTitle"
        personalhelp = PersonalHelp(cbTitle=testTitle)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.cbTitle)

    def test_confirm_cbHref_of_personalHelp_exists(self):
        testHref = "testHref"
        personalhelp = PersonalHelp(cbHref=testHref)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.cbHref)

    def test_confirm_preventionTitle_of_personalHelp_exists(self):
        testTitle = "testTitle"
        personalhelp = PersonalHelp(preventionTitle=testTitle)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.preventionTitle)

    def test_confirm_preventionHref_of_personalHelp_exists(self):
        testHref = "testHref"
        personalhelp = PersonalHelp(preventionHref=testHref)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.preventionHref)

    def test_confirm_helpTitle_of_personalHelp_exists(self):
        testTitle = "testTitle"
        personalhelp = PersonalHelp(helpTitle=testTitle)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.helpTitle)

    def test_confirm_helpHref_of_personalHelp_exists(self):
        testHref = "testHref"
        personalhelp = PersonalHelp(helpHref=testHref)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.helpHref)

    def test_confirm_suiPrevTitle_of_personalHelp_exists(self):
        testTitle = "testTitle"
        personalhelp = PersonalHelp(suiPrevTitle=testTitle)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.suiPrevTitle)

    def test_confirm_suiPrevHref_of_personalHelp_exists(self):
        testHref = "testHref"
        personalhelp = PersonalHelp(suiPrevHref=testHref)
        personalhelp.save()
        self.assertIsNotNone(personalhelp.suiPrevHref)

    def test_confirm_content_of_suiPrevHref(self):
        testHref = "testHref"
        personalhelp = PersonalHelp(suiPrevHref=testHref)
        personalhelp.save()
        self.assertEqual(testHref,personalhelp.suiPrevHref)






####helper methods for the views############

#helper function to add category
def add_cat(name):
    cat = Category(name=name)
    cat.save()
    return cat

####tests for the views############
class HomeViewTests(TestCase):

    def test_home_view_with_no_categories(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_cat('c1')
        add_cat('c2')
        add_cat('c3')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "c3")
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 3)

