from django.db import models
# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.college_name

    def __srt__(self):
        return f"this is a {self.college_name} name"

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name=models.CharField(max_length=100)

class Student(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices = (
        ("Male", "Male"),
        ("Female", "Female")), default="Male")
    phone_number = models.CharField(max_length=30)
    student_bio = models.TextField(editable=False)
    email = models.EmailField()
    date_of_birth = models.DateField()
    created_to = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# student = Student.objects.create(
#     name = "Yasha",
#     age = 24,
#     gender = "Male",
#     phone_number = "+77000777700",
#     student_bio = "Hi, I am a future civil engineer",
#     email = "Yasha05@gmail.com",
#     date_of_birth = "2005-04-03",
#     college = his_college,
#     department = his_department
# )

# colleges = ["UCL", "Imperial", "Berkley", "Austin at TX", "Michigan"]
# departments = ["CS", "Electrical", "Civil", "Mechanical", "Aerospace"]
# skills = ["Python", "English", "Technical Engineering", "Reading drawings", "Procedures knowledge"]


class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)

