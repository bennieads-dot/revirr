from rest_framework import serializers
from api.models import Job
from api.models import Company
from api.models import Assignment
from api.models import Question


class JobSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), many=False)

    assignment = serializers.PrimaryKeyRelatedField(
        queryset=Assignment.objects.all(), many=False)

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
    jobs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id',
                  'name',
                  'city',
                  'street',
                  'description',
                  'logo',
                  'jobs']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id',
                  'title',
                  'prompt',
                  'createdAt',
                  'question_type',
                  'last_updated']

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class AssignmentSerializer(serializers.ModelSerializer):
    jobs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Assignment
        fields = ['id',
                  'name',
                  'time_limit_minutes',
                  'jobs',
                  'questions']

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)
