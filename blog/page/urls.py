from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page_index'),
    path('pages/<int:id>', views.detail)
]