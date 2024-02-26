from django.db import models
from django.conf import settings


# Create your models here.


class DepartmentDB(models.Model):
    DeptId = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=100)


class CourseDB(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=20)
    DeptId = models.ForeignKey(DepartmentDB, on_delete=models.CASCADE)
    Description = models.TextField()


class StudentDB(models.Model):
    StudentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200, null=True, blank=True)
    LastName = models.CharField(max_length=200, null=True, blank=True)
    DateOfBirth = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=1, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    ContactNo = models.IntegerField(blank=True, null=True)
    Address = models.TextField(null=True, blank=True)
    GuardianName = models.CharField(max_length=200, null=True, blank=True)
    GuardianContact = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="StudentsImage")
    EnrollmentID = models.CharField(max_length=20, null=True, blank=True)
    EnrollDate = models.DateField(null=True, blank=True)
    CourseId = models.ForeignKey(CourseDB, on_delete=models.CASCADE, null=True, blank=True)
    Pancard = models.CharField(max_length=50, null=True, blank=True)
    adhaar = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


class FacultyEnrollmentDB(models.Model):
    FacultyID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Joined = models.DateField(null=True, blank=True)
    DeptId = models.ForeignKey(DepartmentDB, on_delete=models.CASCADE)
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Contact = models.CharField(max_length=20, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)


class JobStatus(models.Model):
    STATUS_CHOICES = (
        ('1', 'First interview'),
        ('2', 'Second interview'),
        ('3', 'Offer letter'),
        ('4', 'Rejected'),
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    # You can add more fields as needed, such as timestamp, user reference, etc.

    def __str__(self):
        return self.get_status_display()


class JobsDB(models.Model):
    JobId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=500, null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    image_job = models.ImageField(upload_to="job", null=True, blank=True)
    status = models.ForeignKey(JobStatus, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Title


class JobApplications(models.Model):
    JobId = models.ForeignKey(JobsDB, on_delete=models.CASCADE)
    StudentId = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Resume = models.FileField(upload_to="Resume")


class newsDB(models.Model):
    newsId = models.AutoField(primary_key=True)
    news_Title = models.CharField(max_length=100, null=True, blank=True)
    news_Location = models.CharField(max_length=100, null=True, blank=True)
    news_date = models.DateField(null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    news_image = models.ImageField(upload_to="job", null=True, blank=True)


class newsDB2(models.Model):
    newsId = models.AutoField(primary_key=True)
    news_Title = models.CharField(max_length=100, null=True, blank=True)
    news_Location = models.CharField(max_length=100, null=True, blank=True)
    news_date = models.DateField(null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    news_image = models.ImageField(upload_to="job", null=True, blank=True)


class placed_studdb(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50, null=True, blank=True)
    p_company = models.CharField(max_length=50, null=True, blank=True)
    p_des = models.CharField(max_length=50, null=True, blank=True)
    p_dis = models.CharField(max_length=50, null=True, blank=True)
    p_img = models.ImageField(upload_to="placement", null=True, blank=True)


class Marquee(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
