from rest_framework import serializers
from api.models import Job
from api.models import Company
from api.models import Assignment


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['id',
                  'title',
                  'description',
                  'company',
                  'created',
                  'city',
                  'post_start_date',
                  'post_end_date',
                  'remote',
                  'salary',
                  'last_updated',
                  'assignment']

    def create(self, validated_data):
        return Job.objects.create(**validated_data)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id',
                  'name',
                  'city',
                  'street',
                  'description',
                  'logo']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id',
                  'name',
                  'time_limit_minutes']

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)
