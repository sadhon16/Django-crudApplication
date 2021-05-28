from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:id>', views.Update, name='Update'),
    path('/<int:id>', views.Delete, name='Delete'),
]