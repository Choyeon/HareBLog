"""HareBlog URL配置
urlpatterns列表将URL路由到视图。有关更多信息，请参见：
    https://docs.djangoproject.com/zh-CN/2.2/topics/http/urls/
例子：
功能视图
    1.添加导入：从my_app导入视图
    2.将URL添加到urlpatterns：path（''，views.home，name ='home'）
基于类的视图
    1.添加一个导入：from other_app.views import Home
    2.将URL添加到urlpatterns：path（''，Home.as_view（），name ='home'）
包括另一个URLconf
    1.导入include（）函数：从django.urls导入include，路径
    2.将URL添加到urlpatterns：path（'blog /'，include（'blog.urls'））
"""
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import views as sitemap_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

from comment.views import CommentViewSet
from blog.views import PostViewSet, CategoryViewSet, NavViewSet, TagViewSet
from config.views import LinkViewSet
from user.views import UserViewSet, user_info

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', PostViewSet)
router.register(r'nav', NavViewSet)
router.register(r'tag', TagViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)
router.register(r'link', LinkViewSet)
urlpatterns = [
                  path('admin/', xadmin.site.urls, name='xadmin'),
                  path('', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api-token-auth', obtain_jwt_token),
                  path('user-info', user_info),
                  path('admin/', admin.site.urls, name='admin'),
                  path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
