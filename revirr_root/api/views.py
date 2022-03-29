#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from api.models import Job
from api.serializers import JobSerializer
from api.models import Company
from api.serializers import CompanySerializer
from api.models import Assignment
from api.serializers import AssignmentSerializer
from rest_framework import generics


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class AssignmentList(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
