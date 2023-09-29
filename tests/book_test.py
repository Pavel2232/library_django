import pytest
import faker
from rest_framework.response import Response

from library.models import Book, Author
from library.serializers import BookSerializer

fake = faker.Faker('ru')


@pytest.mark.django_db
def test_list_books(client):
    for _ in range(12):
        Book.objects.create(title=fake.unique.bs())

    response: Response = client.get('/api/books/')
    expected_response = {
        'count': 12,
        'next': 'http://testserver/api/books/?page=2',
        'previous': None,
        'results': BookSerializer(Book.objects.all()[:10], many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response

@pytest.mark.django_db
def test_retrieve_books(client):
    book = Book.objects.create(title=fake.name())

    response = client.get(f'/api/books/{book.pk}')

    expected_response = {
        'id': book.pk,
        'title': book.title,
        'authors': []
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_books(client):
    title = fake.word()
    author = Author.objects.create(title=fake.name())
    response = client.post('/api/books/',
                           {'title': title,
                            'authors': [author.title],
                            }, content_type='application/json'
                           )

    book = Book.objects.get(title=title)
    expected_response = {
        'title': book.title,
        'authors': [author.title]
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_update_book(client):

    now_author = Author.objects.create(title='OldName')

    book = Book.objects.create(title=fake.name())
    book.authors.add(now_author)

    new_author = Author.objects.create(title='ForTest')
    response = client.put(f'/api/books/{book.pk}/',
                          {
                              'title': 'Testowoe',
                              'authors': [new_author.title]
                          }, content_type='application/json'
                          )

    expected_response = {
        'id': book.id,
        'title': 'Testowoe',
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_deleted_books(client):
    book = Book.objects.create(title=fake.name())

    response = client.delete(f'/api/books/{book.id}')

    assert response.status_code == 204
