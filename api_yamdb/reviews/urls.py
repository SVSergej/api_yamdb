from django.urls import path

from . import views

urlpatterns = [
    path('reviews/', views.Review, name='reviews'),
    path('comments/', views.Comments, name='comment'),
]
