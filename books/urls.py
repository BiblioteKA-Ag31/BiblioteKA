from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/list/", views.BookListView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    path("copies/", views.CopyView.as_view()),
    path("books/<int:pk>/copies/", views.CopyDetailsView.as_view()),
]
