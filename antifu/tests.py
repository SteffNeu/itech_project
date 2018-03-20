from django.test import TestCase
from antifu.models import Post,Comment,Category

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
