import json


from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django import views
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework import mixins
from .UsersSerialize import ArticleSerialize

from .models import article
# Create your views here.

class article_view(views.View):
    def get(self, request):
        article_list = article.objects.all()
        article_serial = serializers.serialize('json', article_list )
        a= json.loads(article_serial)
        print(a[0]['fields'])
        print(type(a))


        return HttpResponse(article_serial, content_type='application/json')


    def post(self,request):
        pass





class ArticleListView(APIView):
    """
    列出所有代码片段(snippets), 或者新建一个代码片段(snippet).
    """
    def get(self, request, format=None):
        snippets = article.objects.all()
        serializer = ArticleSerialize(snippets, many=True)
        data = {'code': 8888,'data': serializer.data}

        return Response(data)


from rest_framework.generics import ListCreateAPIView
# GenericViewSet
from rest_framework.mixins import CreateModelMixin
#
# JsonResponse



class ArticleViewSet(viewsets.ModelViewSet):

    queryset = article.objects.all()
    serializer_class = ArticleSerialize

