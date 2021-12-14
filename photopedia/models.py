from django.db import models

# Create your models here.
userType = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
]
DeptChoice = [
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil'),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('FirstYear', 'First Year'),
    ('SecondYear ', 'Second Year '),
    ('ThirdYear', 'Third Year'),
    ('FourthYear', 'Fourth Year'),
]
SemChoice = [
    ('FirstSemester', 'First Semester'),
    ('SecondSemester ', 'Second Semester '),
    ('ThirdSemester', 'Third Semester'),
    ('FourthSemester', 'Fourth Semester'),
    ('FifthSemester', 'Fifth Semester'),
    ('SixthSemester', 'Sixth Semester'),
    ('SeventhSemester', 'Seventh Semester'),
    ('EightthSemester', 'Eightth Semester'),
]
pin_category = [
    ('Campus', 'Campus'),
    ('Carrer', 'Carrer'),
    ('Culture', 'Culture'),
    ('Sports', 'Sports'),
    ('Teacher', 'Teacher'),
    ('Sudent', 'Sudent'),
]


class Account(models.Model):
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    password_confirm = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    department = models.CharField(
        max_length=50,
        choices=DeptChoice,
        default='Computer Science'
    )
    year = models.CharField(
        max_length=50,
        choices=YearChoice,
        default=None,
        blank=True,
        null=True
    )
    semester = models.CharField(
        max_length=50,
        choices=SemChoice,
        default=None,
        blank=True,
        null=True
    )
    enrollment = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    profile_pic = models.ImageField(
        upload_to="img/user/",
        blank=True,
        null=True
    )
    user_type = models.CharField(
        max_length=50,
        choices=userType,
        default='Student'
    )
    active = models.BooleanField(default=True)

    def is_student(self):
        return self.user_type == 'student'

    def is_teacher(self):
        return self.user_type == 'teacher'

    def name(self):
        return self.first_name + ' ' + self.last_name


class Pin(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/pin/", null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    tag = models.TextField(max_length=100, null=True, blank=True)
    details = models.TextField(max_length=1000, null=True, blank=True)
    category = models.CharField(
        max_length=50,
        choices=pin_category,
        default='Campus'
    )
    create_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
