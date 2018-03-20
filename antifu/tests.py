from django.test import TestCase
from antifu.models import Post,Comment,Category
from datetime import date

# Create your tests here.
class PostMethodTests(TestCase):

    def test_ensure_grammarFail_is_positive(self):
        # create test category for reference
        cat = Category(name="test")
        cat.save()
        post = Post(category=cat,grammarFail=0)
        post.save()
        self.assertEqual((post.grammarFail >= 0), True)

    def test_ensure_logicFail_is_positive(self):
        # create test category for reference
        cat = Category(name="test")
        cat.save()
        post = Post(category=cat,logicFail=0)
        post.save()
        self.assertEqual((post.logicFail >= 0), True)

    def test_ensure_toxicity_is_positive(self):
        # create test category for reference
        cat = Category(name="test")
        cat.save()
        post = Post(category=cat,toxicity=0)
        post.save()
        self.assertEqual((post.toxicity >= 0), True)

    def test_ensure_harmful_is_positive(self):
        # create test category for reference
        cat = Category(name="test")
        cat.save()
        post = Post(category=cat,harmful=0)
        post.save()
        self.assertEqual((post.harmful >= 0), True)

    def test_ensure_correct_date(self):
        # create test category for reference
        cat = Category(name="test")
        cat.save()
        post = Post(category=cat)
        post.save()
        #get current date
        today = date.today()
        self.assertEqual((post.date == today), True)

    def test_ensure_id_increment(self):
        cat = Category(name="test")
        cat.save()
        first_post = Post(category=cat)
        first_post.save()
        second_post = Post(category=cat)
        second_post.save()

        self.assertIs(1,second_post.id-first_post.id)

    def test_ensure_category(self):
        i = 3
        #post = Post()
        #post.save()