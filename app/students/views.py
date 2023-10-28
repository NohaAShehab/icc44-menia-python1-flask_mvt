from flask import  request, render_template, redirect, url_for
from app.models import  Student, Track
from app.students import student_blueprint


@student_blueprint.route('', endpoint='index')
def students_index():
    students=  Student.get_all_students()
    return render_template('students/index.html', students=students)

@student_blueprint.route('/<int:id>', endpoint='show')
def student_show(id):
    student=  Student.get_specific_student(id)
    return render_template('students/show.html', student=student)

@student_blueprint.route('/<int:id>/delete', endpoint='delete')
def student_delete(id):
    Student.delete_object(id)
    # redirect
    return  redirect(url_for('students.index'))

@student_blueprint.route('/create', endpoint='create', methods = ['GET', 'POST'])
def student_create():
    tracks = Track.get_all_tracks()
    print(f'Request received {request}')
    if request.method=='POST':
        print(request.form)
        student = Student.save_object(requestdata=request.form)
        return redirect(student.show_url)

    return render_template('students/create.html', tracks=tracks)
