from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('job/', views.JobList.as_view()),
    path('job/<int:pk>/', views.JobDetail.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('assignment/', views.AssignmentList.as_view()),
    path('assignment/<int:pk>/', views.AssignmentDetail.as_view()),
    path('question/', views.QuestionList.as_view()),
    path('question/<int:pk>/', views.QuestionDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
