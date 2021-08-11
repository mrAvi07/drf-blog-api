from django.urls import path
from .api.views import home_view, detail_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home_view, name="home"),
    path('blog-detail/<int:pk>/', detail_view, name="blog-detail"),
    path('auth-token/', obtain_auth_token, name="auth-token"),
]
