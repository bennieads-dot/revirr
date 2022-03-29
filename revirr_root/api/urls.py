from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('jobs/', views.JobList.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('assignment/', views.AssignmentList.as_view()),
    path('assignment/<int:pk>/', views.AssignmentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
