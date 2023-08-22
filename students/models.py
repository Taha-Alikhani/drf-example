from django.db import models
from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.slug
