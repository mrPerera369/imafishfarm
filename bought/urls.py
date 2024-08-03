# bought/urls.py
from django.urls import path
from . import views

app_name = 'bought'  # Ensure this line is present

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),  # Ensure this line is correct
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
]
