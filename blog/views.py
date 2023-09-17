from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog import serializers
from blog.models import Article
from blog.pagination import CustomPagination


class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-updated_at')
    serializer_class =  serializers.ArticleListSrializer
    search_fields = ['title', 'text']
    pagination_class = CustomPagination


class ArticleDetailView(APIView):
    def get(self, request, slug):
        queryset = get_object_or_404(Article, slug=slug)
        serializer_class = serializers.ArticleDetailSrializer(instance=queryset, context={'request': request})
        return Response(serializer_class.data)
        

class CategoryDetailView(APIView):
    def get(self, request, pk):
        queryset = Article.objects.filter(status=True).filter(category__id=pk).order_by('-updated_at')
        serializer_class =  serializers.ArticleListSrializer(instance=queryset, context={'request': request}, many=True)
        return Response(serializer_class.data)
 

class TagDetailView(APIView):
    def get(self, request, pk):
        queryset = Article.objects.filter(status=True).filter(tag__id=pk).order_by('-updated_at')
        serializer_class =  serializers.ArticleListSrializer(instance=queryset, context={'request': request}, many=True)
        return Response(serializer_class.data)