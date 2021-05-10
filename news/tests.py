from django.test import TestCase
from .models import Article,Editor,tags

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