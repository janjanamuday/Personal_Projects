from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_entry/<int:pk>', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:pk>', views.delete_entry, name='delete_entry'),

    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_students'),
    path('edit_student/<int:pk>', views.edit_student,name='edit_student'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('delete_books/<int:pk>', views.delete_book, name='delete_books'),
]