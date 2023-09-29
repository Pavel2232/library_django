from rest_framework import serializers

from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Book
        fields = ['title', 'authors']


class CreateBookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Author.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Book
        fields = ['title', 'authors']

    def is_valid(self, raise_exception=False):
        self._authors = self.initial_data.pop('authors')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)

        for author in self._authors:
            author_obj, _ = Author.objects.get_or_create(title=author)
            book.authors.add(author_obj)

        return book


class UpdateRetrieveSerializers(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Author.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Book
        fields = '__all__'

    def update(self, book: Book, validated_data):
        book.title = validated_data.get("title", book.title)
        book.authors.set(validated_data.get('authors'))
        book.save()
        return book
