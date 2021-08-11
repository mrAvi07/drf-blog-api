from rest_framework.views import APIView
from ..models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status

class HomeView(APIView):

    permission_classes = [ IsAuthenticated ]

    def get(self, request,*args, **kwargs):
        query_Set = Blog.objects.all()
        serializer = BlogSerializer(query_Set, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DetailView(APIView):

    permissions_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogSerializer(blog_post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogSerializer(blog_post)
        serializer.delete()




home_view = HomeView.as_view()

detail_view = DetailView.as_view()
