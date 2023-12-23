from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Review, Author, Genre, FavoriteBook
from .serializers import BookSerializer, ReviewCreateSerializer, ReviewSerializer, FavoriteSerializer, \
    RegistrationSerializer


# Create your views here.

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer


class BooksListView(APIView):

    def get(self, request):
        queries = ('author', 'genre', 'title')
        for q in queries:
            query = self.request.query_params.get(q, '')  # take a title param from url
            if query:
                break

        if query and q == 'title':
            print('Found', q)
            queryset = Book.objects.filter(
                title__icontains=query
            )  # filter books by title
            serializer = BookSerializer(queryset, many=True)

            return Response({'books': serializer.data})  # if title param exists
        elif query and q not in ('author', 'genre'):
            if q == 'author':
                queryset = Author.objects.get(name__icontains=query)
                queryset = Book.objects.filter(
                author=queryset)

            elif q == 'genre':
                queryset = Genre.objects.get(name__icontains=query)
                queryset = Book.objects.filter(
                genre=queryset)  # filter books by title

            serializer = BookSerializer(queryset, many=True)

            return Response({'books': serializer.data})

        queryset = Book.objects.all()
        print('query dont found')
        serializer = BookSerializer(queryset, many=True)
        return Response({'books': serializer.data}) # return all books


class BookDetailAPIView(APIView):

    def get(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            reviews = Review.objects.all()
        except Book.DoesNotExist:
            raise Http404
        serializer = BookSerializer(book)
        review_serializer = ReviewSerializer(reviews, many=True)
        return Response({book.title: serializer.data,
                         'reviews': review_serializer.data})


class BookReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.kwargs.get('pk')  # Получаем идентификатор книги из URL
        book = Book.objects.get(pk=book_id)
        serializer.save(book=book, user=self.request.user)  # С


class FavoriteCreateAPIView(CreateAPIView):
    queryset = FavoriteBook.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoritesListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = FavoriteBook.objects.filter(user=request.user)
        serializer = FavoriteSerializer(queryset, many=True)
        return Response({'favorites': serializer.data})

