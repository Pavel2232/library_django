import pytest
import faker
from rest_framework.response import Response

from library.models import Author
from library.serializers import AuthorSerializer

fake = faker.Faker('ru')


@pytest.mark.django_db
def test_list_authors(client):
    for _ in range(12):
        Author.objects.create(title=fake.unique.name())

    response: Response = client.get('/api/authors/')
    expected_response = {
        'count': 12,
        'next': 'http://testserver/api/authors/?page=2',
        'previous': None,
        'results': AuthorSerializer(Author.objects.all()[:10], many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve_author(client):
    author = Author.objects.create(title=fake.name())

    response = client.get(f'/api/authors/{author.pk}/')

    expected_response = {
        'id': author.pk,
        'title': author.title
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_author(client):
    title = fake.name()
    response = client.post('/api/authors/',
                           {'title': title}
                           )

    author = Author.objects.get(title=title)
    expected_response = {
        'id': author.id,
        'title': author.title
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_update_author(client):
    author = Author.objects.create(title=fake.name())
    response = client.put(f'/api/authors/{author.pk}/',
                          {
                              'title': 'Test'
                          }, content_type='application/json'
                          )

    expected_response = {
        'id': author.pk,
        'title': 'Test'
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_deleted_author(client):
    author = Author.objects.create(title=fake.name())

    response = client.delete(f'/api/authors/{author.pk}/',)

    assert response.status_code == 204

