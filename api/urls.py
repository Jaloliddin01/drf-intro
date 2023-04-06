from django.urls import path
from .views import (
    hi,
    addition,
    subtraction,
    multiplication,
    division,
    AdditionView,
    SubtractionView,
    MultiplicationView,
    DivisionView
)

urlpatterns = [
    path('hi', hi),
    path('addition', AdditionView.as_view()),
    path('subtraction', SubtractionView.as_view()),
    path('multiplication', MultiplicationView.as_view()),
    path('division', DivisionView.as_view()),
]
