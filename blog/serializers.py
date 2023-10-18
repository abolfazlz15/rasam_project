from rest_framework import serializers

from blog.models import Article, Tag, Category
from utils.date_conversion.utils import jajali_converter


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ArticleListSrializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='full_name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'slug', 'title', 'image', 'author', 'category')


class ArticleDetailSrializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='full_name')
    id = serializers.IntegerField(read_only=True)
    tag = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Article
        exclude = ('status', 'updated_at', 'slug')

    def get_cover(self, obj):
        request = self.context.get('request')
        # add base URL for cover music
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None

    def get_tag(self, obj):
        serializer = TagSerializer(instance=obj.tag)
        return serializer.data

    def get_category(self, obj):
        serializer = CategorySerializer(instance=obj.category)
        return serializer.data

    def get_created_at(self, obj):
        date = obj.created_at
        return jajali_converter(date)
    

class CategoryListSrializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')