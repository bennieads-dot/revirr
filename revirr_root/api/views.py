from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Job
from api.serializers import JobSerializer


@api_view(['GET', 'POST'])
def JobList(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
