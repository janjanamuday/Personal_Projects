from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from library.models import Student, Book, Library
from .serializers import StudentSerializer, BookSerializer, LibrarySerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "----------------": "----------",
        'Display Students': 'students',
        'Add Student': 'create_student',
        'View Student': 'student/<int:pk>',
        'Delete Student': 'delete_student/<int:pk>',
        'Update Student': 'update_student/<int:pk>',
        "----------------": "----------",
        'Display Books': 'books',
        'Add Book': 'create_book',
        'View Book': 'book/<int:pk>',
        'Delete Book': 'delete_book/<int:pk>',
        'Update Book': 'update_book/<int:pk>',
        "----------------": "----------",
        'Display Libraries': 'libraries',
        'Add Library': 'create_library',
        'View Library': 'library/<int:pk>',
        'Delete Library': 'delete_library/<int:pk>',
        'Update Library': 'update_library/<int:pk>',
    }
    return Response(api_urls)

# Student Views
@api_view(['GET'])
def show_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_Student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    print("Errors:", serializer.errors)  # Debugging line
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response("Student Successfully Deleted", status=status.HTTP_204_NO_CONTENT)

# Book Views
@api_view(['GET'])
def show_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(instance=book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return Response("Book Successfully Deleted", status=status.HTTP_204_NO_CONTENT)

# Library Views
@api_view(['GET'])
def show_libraries(request):
    libraries = Library.objects.all()
    serializer = LibrarySerializer(libraries, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_library(request):
    serializer = LibrarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_library(request, pk):
    library = get_object_or_404(Library, id=pk)
    serializer = LibrarySerializer(instance=library, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_library(request, pk):
    library = get_object_or_404(Library, id=pk)
    serializer = LibrarySerializer(library)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_library(request, pk):
    library = get_object_or_404(Library, id=pk)
    library.delete()
    return Response("Library Successfully Deleted", status=status.HTTP_204_NO_CONTENT)
