from django.test import TestCase
from django.contrib.auth.models import User
from antifu.models import Post,Comment,Category,UserProfile
from datetime import date

# Create your tests here.
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

    def test_ensure_category(self):
        i = 3
        #post = Post()
        #post.save()

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