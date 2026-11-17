from django.db import models
class Module(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    def __str__(self): return f"{self.code} - {self.name}"
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    enrolmentDate = models.DateTimeField()
    modules = models.ManyToManyField(Module, blank=True)\n    image = models.ImageField(upload_to='student_images/', blank=True)
    def __str__(self): return f"{self.firstName} {self.lastName}"
