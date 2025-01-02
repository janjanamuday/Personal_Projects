from library.models import Student, Book, Library
from rest_framework import serializers



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'student_class', 'photo', 'video']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author_name', 'publication', 'year']

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'student', 'book', 'start_date', 'end_date']
