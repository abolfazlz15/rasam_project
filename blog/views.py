from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Article
from blog import serializers


class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-updated_at')
    serializer_class =  serializers.ArticleListSrializer
    search_fields = ['title', 'text']
    