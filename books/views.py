from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Recommendation
from .serializers import BookSerializer, RecommendationSerializer
from .services import fetch_books
from django.shortcuts import render

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['post'])
    def fetch_books(self, request):
        query = request.data.get('query', '')
        books_data = fetch_books(query)
        books = []
        for item in books_data:
            volume_info = item['volumeInfo']
            book, created = Book.objects.get_or_create(
                title=volume_info['title'],
                author=volume_info['authors'][0] if volume_info.get('authors') else 'Unknown',
                description=volume_info.get('description', ''),
                cover_image=volume_info['imageLinks']['thumbnail'] if volume_info.get('imageLinks') else '',
                rating=volume_info.get('averageRating', 0)
            )
            books.append(book)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer



def index(request):
    return render(request, 'index.html')
