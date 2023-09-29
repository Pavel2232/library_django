from django.db import models


class Author(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Название книги')
    authors = models.ManyToManyField(Author, related_name='books', verbose_name='Авторы')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
