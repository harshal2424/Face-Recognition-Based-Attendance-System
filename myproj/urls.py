# myproj/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp import views # For main application views
#from myapp import views_yolo # For the separate YOLO processing view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_default'),
    path('login/', views.login_view, name='login'),
    # Path using the process_image function from views_yolo.py
    #path('upload/', views_yolo.process_image, name='process_image'),
    # Path using the result view from the main views.py
    path('result/', views.result, name='result'),
    # Corrected name typo below
    path('attendance_failed/', views.attendance_failed, name='attendance_failed'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    # path('direct_attendance/', views.direct_attendance, name='direct_attendance'), # Keep commented if not used
    path('attendance_success/', views.attendance_success, name='attendance_success'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_course/', views.create_course_view, name='create_course'),
    # Removed duplicate add_subject path below
    path('add_subject/', views.add_subject_view, name='add_subject'),
    path('instructor_dashboard/', views.instructor_dashboard_view, name='instructor_dashboard'),
    path('ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects'),
    path('manage_courses/', views.manage_courses_view, name='manage_courses'),
    path('manage_course/<int:course_id>/students/', views.manage_course_students_view, name='manage_course_students'),
    path('delete_course/<int:course_id>/', views.delete_course_view, name='delete_course'),
    path('export_attendance/<int:course_id>/', views.export_attendance_excel, name='export_attendance_excel'),
]

# Pattern for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)