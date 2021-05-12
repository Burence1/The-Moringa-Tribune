from news.views import article
from django.test import TestCase
from .models import Article,Editor,tags
import datetime as dt

class EditorTestClass(TestCase):
  #setup
  def setUp(self):
    self.Burens=Editor(first_name= 'Burens',last_name= 'Omondi', email= 'burensdev@gmail.com')

# Create your tests here.

#testing instance

  def test_instance(self):
    self.assertTrue(isinstance,(self.Burens,Editor))

  def test_save(self):
    self.Burens.save_editor()
    editors=Editor.objects.all()
    self.assertTrue(len(editors)>0)
  
  def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Article.objects.all().delete()

class ArticleTestClass(TestCase):
  def setUp(self):
        # Creating a new editor and saving it
        self.Burens= Editor(first_name = 'Burens', last_name ='Omondi', email ='burensdev@gmail.com')
        self.Burens.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.Burens)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

  def tearDown(self):
      Editor.objects.all().delete()
      tags.objects.all().delete()
      Article.objects.all().delete()

  def test_get_news_by_date(self):
      test_date = '2017-03-17'
      date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
      news_by_date = Article.days_news(date)
      self.assertTrue(len(news_by_date) == 0)

  def test_delete_article(self):
      self.new_article.save_article()
      articles=Article.objects.all()
      self.assertEqual(len(articles),1)
      self.new_article.delete_article()
      new_articles=Article.objects.all()
      self.assertEqual(len(new_articles),0)
  
  def test_displaying_todays_news(self):
      self.new_article.save_article()
      self.assertEqual(len(Article.todays_news()),1)

  def test_updating_article(self):
      self.new_article.save_article()
      self.new_article.update_article(self.new_article.id,'latest')
      update= Article.objects.get(title='latest')
      self.assertEqual(update.title,'latest')