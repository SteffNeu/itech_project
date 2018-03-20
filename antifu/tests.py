from django.test import TestCase
from django.contrib.auth.models import User
from antifu.models import Post,Comment,Category,UserProfile
from datetime import date

# Create your tests here.
class PostMethodTests(TestCase):

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

    def test_ensure_correct_date(self):
        post = Post(category=self.cat)
        post.save()
        #get current date
        today = date.today()
        self.assertEqual((post.date == today), True)

    def test_ensure_id_increment(self):
        first_post = Post(category=self.cat)
        first_post.save()
        second_post = Post(category=self.cat)
        second_post.save()
        self.assertIs(1,second_post.id-first_post.id)

    def test_ensure_category(self):
        i = 3
        #post = Post()
        #post.save()

    def test_confirm_user(self):
        post = Post(category=self.cat,user=self.u_profile)
        post.save()
        self.assertIsNotNone(post.user)

    def test_confirm_title_of_post(self):
        testTitle = "Some title"
        post = Post(category=self.cat,title=testTitle)
        post.save()
        self.assertIsNotNone(post.title)
        self.assertEqual(testTitle,post.title)

    def test_confirm_content_of_title(self):
        testTitle = "Some title"
        post = Post(category=self.cat,title=testTitle)
        post.save()
        self.assertEqual(testTitle,post.title)

    def test_confirm_content_of_context(self):
        testContext = "The context of the post"
        post = Post(category=self.cat,context=testContext)
        post.save()
        self.assertEqual(testContext,post.context)