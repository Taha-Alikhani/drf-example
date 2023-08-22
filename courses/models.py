from django.db import models


class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField('students.Student',
                                      related_name='courses_joined',
                                      blank=True)
    capacity = models.PositiveIntegerField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
