# myapp/models.py
# myapp/models.py

from django.db import models
# Consider importing User model if you implement instructor linking later
# from django.contrib.auth.models import User

class UploadedFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    processed_faces = models.JSONField(default=list, blank=True)
    processed_file = models.ImageField(upload_to='processed/', blank=True, null=True)
    def __str__(self):
        return f"Uploaded File: {self.file.name} - Processed: {bool(self.processed_file)}"
    class Meta:
        db_table = 'Uploaded & Processed Files'


class Students(models.Model):
    name = models.CharField(max_length=100, null=True)
    roll_no = models.CharField(max_length=25, null=True, unique=True)
    photo = models.FileField(upload_to='student_photos/', blank=True, null=True)
    def __str__(self):
        return f"Student: {self.name} - Roll No: {self.roll_no}"

    class Meta:
        db_table = 'Student Details'

class Course(models.Model):
    name = models.CharField(max_length=55)
    students = models.ManyToManyField(Students, blank=True, related_name='courses') # <-- ADDED ManyToManyField

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.name} ({self.course.name})"

    class Meta:
        db_table = 'Subjects'
        unique_together = ('name', 'course')


class ClassroomGroup(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom_image = models.ImageField(upload_to='classroom_images/')
    def __str__(self):
        return f"Classroom Group: {self.date} - Course: {self.course.name}"
    class Meta:
        db_table = 'Classroom photos'


class Attendance(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    status = models.CharField( max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")], default="Absent")
    photo = models.ImageField(upload_to="attendance_photos/", blank=True, null=True)
    class Meta:
        unique_together = ('date', 'course', 'student')
        db_table = 'attendance_records'
    def __str__(self):
        return f"{self.date} | {self.course.name} | {self.student.name} | {self.status}"