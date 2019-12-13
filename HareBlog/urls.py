"""HareBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.sitemaps import views as sitemap_views
from django.conf.urls.static import static
from django.conf import settings

from comment.views import CommentViewSet
from blog.views import PostViewSet,CategoryViewSet,NavViewSet,TagViewSet
from user.views import UserViewSet

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', PostViewSet)
router.register(r'nav', NavViewSet)
router.register(r'user', UserViewSet)
router.register(r'tag', TagViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'comment', CommentViewSet)
urlpatterns = [
                  # path('', IndexView.as_view(), name='index'),
                  path('', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # re_path(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name='category-list'),
                  # re_path(r'^tag/(?P<tag_id>\d+)/', TagView.as_view(), name='tag-list'),
                  # re_path(r'^post/(?P<post_id>\d+).html', PostDetail.as_view(), name='post-detail'),
                  # path('links/', LinkListView.as_view(), name='links'),
                  # path('super_admin/', admin.site.urls, name='super-admin'),
                  path('admin/', admin.site.urls, name='admin'),
                  # path('search/', SearchView.as_view(), name="search"),
                  # re_path(r'^author/(?P<owner_id>\d+)/', AuthorView.as_view(), name='author'),
                  # path('comment/', CommentView.as_view(), name='comment'),
                  # re_path('^rss|feed/', LatestPostFeed(), name='rss'),
                  re_path(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
              ]
