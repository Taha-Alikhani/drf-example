from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course
from .serializers import StudentSerializer


class StudentAPIView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EnrollStudentAPIView(APIView):
    def post(self, request, course_id, student_id):
        try:
            course = Course.objects.get(slug=course_id)
            student = Student.objects.get(slug=student_id)
        except (Course.DoesNotExist, Student.DoesNotExist):
            return Response("Course or student does not exist", status=404)

        if course.students.count() < course.capacity:
            course.students.add(student)
            student.courses.add(course)
            return Response("Student enrolled successfully", status=200)
        else:
            return Response("Course is already full", status=400)
