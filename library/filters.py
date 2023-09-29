import django_filters
from library.models import Book


class BookFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Book
        fields = ("title",)
