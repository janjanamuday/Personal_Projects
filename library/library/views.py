from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Book, Library

def index(request):
    library = Library.objects.all()
    students = Student.objects.all()
    books = Book.objects.all()
    if request.method=='POST':
        student_name = request.POST.get('student_name')
        book_name = request.POST.get('book_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        data = Library(name_id=student_name, book_id=book_name, start_date=start_date, end_date=end_date)
        data.save()
        return redirect('index')
    context = {
        'library': library,
        'students': students,
        'books': books
    }
    return render(request, 'index.html', context)

def delete_entry(request, pk):
    entry = Library.objects.get(id=pk)
    entry.delete()
    return redirect('index')

def edit_entry(request, pk):
    entry = get_object_or_404(Library, id=pk)
    students = Student.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        edit_student_name = request.POST.get('edit_student_name')
        edit_book_name = request.POST.get('edit_book_name')
        edit_start_date = request.POST.get('edit_start_date')
        edit_end_date = request.POST.get('edit_end_date')

        # Update only if new values are provided; otherwise, keep the old values
        if edit_student_name:
            entry.name_id = edit_student_name
        if edit_book_name:
            entry.book_id = edit_book_name
        if edit_start_date:
            entry.start_date = edit_start_date
        if edit_end_date:
            entry.end_date = edit_end_date

        entry.save()
        return redirect('index')

        return redirect('index')

    context = {
        'entry': entry,
        'students': students,
        'books': books,
    }

    return render(request, 'edit_entry.html', context)


def add_student(request):
    students = Student.objects.all()

    if request.method== 'POST':
        name = request.POST.get('name')
        classs = request.POST.get('class')
        photo = request.FILES.get('photo')
        video = request.FILES.get('video')

        data = Student(student_name=name, student_class=classs, photo=photo, video=video)
        data.save()
        return redirect('add_student')

    context = {
        'students': students
    }
    return render(request, 'add_student.html', context)

def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('add_student')


def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_classs = request.POST.get('edit_class')
        edit_photo = request.FILES.get('edit_photo')
        edit_video = request.FILES.get('edit_video')

        # Update the student object with provided values or keep the existing ones
        student.student_name = edit_name if edit_name else student.student_name
        student.student_class = edit_classs if edit_classs else student.student_class

        if edit_photo:
            student.photo = edit_photo
        if edit_video:
            student.video = edit_video

        student.save()
        return redirect('add_student')

    context = {
        'student': student
    }
    return render(request, 'edit_student.html', context)

def add_book(request):
    books = Book.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        publication = request.POST.get('publication')
        year = request.POST.get('year')

        data = Book(book_name=name, author_name=author, publication=publication, year=year)
        data.save()
        return  redirect('add_book')
    context = {
        'books': books
    }
    return render(request, 'book.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('add_book')

def edit_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_author = request.POST.get('edit_author')
        edit_publication = request.POST.get('edit_publication')
        edit_year = request.POST.get('edit_year')

        data = Book(id=pk,book_name=edit_name, author_name=edit_author, publication=edit_publication, year=edit_year)
        data.save()
        return redirect('add_book')
    context = {
        'book': book
    }
    return render(request, 'edit_book.html', context)