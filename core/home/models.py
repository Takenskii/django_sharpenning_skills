from django.db import models
# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name=models.CharField(max_length=100)

class Student(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
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
#     name = "Simmy",
#     age = 20,
#     gender = "Female",
#     phone_number = "+77000777777",
#     student_bio = "Hi, I am a future business manager",
#     email = "simmy04@gmail.com",
#     date_of_birth = "2005-11-11"
# )

# colleges = ["UCL", "Imperial", "Berkley", "Austin at TX", "Michigan"]
