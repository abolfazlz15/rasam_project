from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from blog.models import Article
from blog import serializers
from rest_framework.response import Response

class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-updated_at')
    serializer_class =  serializers.ArticleListSrializer
    search_fields = ['title', 'text']


class ArticleDetailView(APIView):
    def get(self, request, slug):
        queryset = get_object_or_404(Article, slug=slug)
        serializer_class = serializers.ArticleDetailSrializer(instance=queryset, context={'request': request})
        return Response(serializer_class.data)