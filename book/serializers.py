from rest_framework import serializers

from .models import Book, Review, FavoriteBook, CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')


class BookSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        if user and user.is_authenticated:
            return FavoriteBook.objects.filter(user=user, book=obj).exists()
        return False


# serializers.py

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('book', 'user', 'rating', 'text', 'created_at')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'text']


class FavoriteSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=Book.objects.all())

    class Meta:
        model = FavoriteBook
        fields = '__all__'
