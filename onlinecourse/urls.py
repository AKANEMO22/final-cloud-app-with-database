from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    path(route='course/<int:pk>/enroll/', view=views.EnrollView.as_view(), name='enroll'),
    path(route='course/<int:pk>/', view=views.CourseDetailsView.as_view(), name='course_details'),
    
    # Task 6: Paths for submit and show_exam_result
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
