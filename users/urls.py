from django.urls import path
from users.views import SignupView, LoginUserView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginUserView.as_view()),
]