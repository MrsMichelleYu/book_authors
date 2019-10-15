from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_book),
    url(r'^books/(?P<id>\d+)$', views.book_description),
    url(r'^add_author_id/(?P<id>\d+)$', views.add_author_id),
    url(r'^authors$', views.authors),
    url(r'^add_authors$', views.add_author),
    url(r'^authors/(?P<id>\d+)$', views.author_description),
    url(r'^add_book_id/(?P<id>\d+)$', views.add_book_id),
]