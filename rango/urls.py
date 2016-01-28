from django.conf.urls import patterns, url
from . import views

urlpatterns = [
                url(r'^$', views.index, name='index'),
                url(r'^about', views.about, name='about'),
                url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                url(r'^add_category/$', views.add_category, name='add_category'),
                url(r'^add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),
                url(r'^register/$', views.register, name='register'),
              ]