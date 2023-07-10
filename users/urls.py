from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),

    path("users/book/", views.UserBookView.as_view()),
    path("users/<int:pk>/", views.UserDetailsView.as_view()),


    path("users/<int:pk>/", views.UserDetailsView.as_view()),
    path("users/books/<int:pk>/", views.UserBookView.as_view()),

    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("sendmail/", views.SendEmailView.as_view()),
]
