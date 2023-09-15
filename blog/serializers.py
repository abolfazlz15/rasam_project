from rest_framework import serializers

from blog.models import Article


class ArticleListSrializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='full_name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'slug', 'title', 'image', 'author', 'category')


class ArticleDetailSrializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
    tag = serializers.SlugRelatedField(read_only=True, slug_field='title')
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='full_name')
    id = serializers.IntegerField(read_only=True)

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


 