from django.urls import path

from library.views import AuthorViewSet, ListCreateBookAPIView, RetrieveBookAPIView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('books/', ListCreateBookAPIView.as_view(), name='books'),
    path('books/<int:pk>', RetrieveBookAPIView.as_view(), name='retrieve-book'),
]
urlpatterns += router.urls
