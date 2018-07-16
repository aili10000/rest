"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from appss.users.views import article_view
from rest_framework.documentation import include_docs_urls
from appss.users.views import ArticleListView,ArticleViewSet

router = routers.DefaultRouter()
router.register('artviewset', ArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', article_view.as_view()),
    path('docs/', include_docs_urls(title='shenleis api')),
    path('api-auth/', include('rest_framework.urls')),
    path('article/', ArticleListView.as_view()),
    path('main/', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),

    # url(r'^api-auth/', include('rest_framework.urls'))
    # url(r'^api-token-auth/', obtain_jwt_token),
]
