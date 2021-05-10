from django.contrib import admin
from .models import Article,Editor,tags

# Register your models here.

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)