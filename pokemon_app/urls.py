# Django
from django.urls import include, path

# Views
from . import views

urlpatterns = [
    path('search/<str:name>/', views.search, name='search'),
]
