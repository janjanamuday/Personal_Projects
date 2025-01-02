from django.db import models

# Create your models here.
#Student Creation Model
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    photo = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return self.student_name

# Book Creation Model
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return self.book_name


# Library
class Library(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
