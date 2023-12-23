"""
URL configuration for BookCatalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path

from book.views import BooksListView, BookDetailAPIView, BookReviewCreateAPIView, FavoriteCreateAPIView, \
    FavoritesListAPIView, RegistrationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/register/', RegistrationAPIView.as_view(), name='register'),
    path('api/v1/books/', BooksListView.as_view(), name='books'),
    path('api/v1/books/<int:pk>/', BookDetailAPIView.as_view(), name='books-detail'),
    path('api/v1/books/<int:pk>/reviews/', BookReviewCreateAPIView.as_view(), name='book-review'),
    path('api/v1/books/<int:pk>/favorites/add/', FavoriteCreateAPIView.as_view(), name='add-to-favorites'),
    path('api/v1/books/favorites/', FavoritesListAPIView.as_view(), name='favorites'),
]
