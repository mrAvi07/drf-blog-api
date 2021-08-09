from rest_framework import serializer
from ..models import Blog, Category


class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']



class BlogSerializer(serializer.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'body']
