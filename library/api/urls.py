from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),

    path('students/', views.show_students, name='students'),
    path('student/<int:pk>/', views.view_student, name='student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('create_student/', views.create_Student, name='create_student'),


    path('books/', views.show_books, name='books'),
    path('book/<int:pk>/', views.view_book, name='book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('create_book/', views.create_book, name='create_book'),

    path('libraries/', views.show_libraries, name='libraries'),
    path('library/<int:pk>/', views.view_library, name='library'),
    path('update_library/<int:pk>/', views.update_library, name='update_library'),
    path('delete_library/<int:pk>/', views.delete_library, name='delete_library'),
    path('create_library/', views.create_library, name='create_library'),
]
