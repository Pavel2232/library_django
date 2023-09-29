from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from library.filters import BookFilter
from library.models import Author, Book
from library.serializers import AuthorSerializer, CreateBookSerializer, UpdateRetrieveSerializers


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListCreateBookAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter


class RetrieveBookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = UpdateRetrieveSerializers
