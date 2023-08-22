from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'overview', 'created',
                  'professor', 'students', 'capacity',]
