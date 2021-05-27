from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

urlpatterns = [
  path('',views.news_today,name='newsToday'),
  re_path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
  path('search/',views.search_results,name='search_results'),
  path('article/(\d+)', views.article, name='article'),
  path('new-article',views.new_article, name='new-article'),
  path('ajax/newsletter/', views.newsletter, name='newsletter'),
  path('api/merch/merch-id/<int:pk>/',views.MerchDescription.as_view())
  # path('api/merch/', views.MerchList.as_view()),
  # re_path('api/merch/merch-id/(?P<pk>[0-9]+)/',
  #     views.MerchDescription.as_view())
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
