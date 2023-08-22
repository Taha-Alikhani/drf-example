from django.urls import path
from .views import StudentAPIView, EnrollStudentAPIView

urlpatterns = [
    path('', StudentAPIView.as_view(), name='students'),
    path('enroll/<str:student_id>/<str:course_id>/', EnrollStudentAPIView.as_view(), name='enroll_student'),
]
