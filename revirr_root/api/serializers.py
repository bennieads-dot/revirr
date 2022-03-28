from rest_framework import serializers
from api.models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['id',
                  'title',
                  'description',
                  'company',
                  'submitted_time']

    def create(self, validated_data):
        return Job.objects.create(**validated_data)
