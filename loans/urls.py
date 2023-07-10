from django.urls import path
from . import views

urlpatterns = [
    path("loans/", views.LoanView.as_view()),
    path("loans/list/", views.LoanListView.as_view()),
    path("loans/<int:pk>/", views.LoanDetailView.as_view()),
]
