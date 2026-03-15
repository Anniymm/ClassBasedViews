from django.db import models

# foreignkey - > erti bevrtan 
# manyto many -> ManytoManyField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True, null=True)

    def __str__(self):
        return self.name
    


