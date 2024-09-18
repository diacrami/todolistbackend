from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
         model = Tasks
         fields= '__all__'


class TasksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('__all__')

    def create(self, validated_data):
        task = Tasks.objects.create(**validated_data)

        return task

class TasksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('taskname', 'state', 'isActive')

    def update(self, instance, validated_data):
        instance.taskname = validated_data.get("taskname", instance.taskname)
        instance.state = validated_data.get("state", instance.state)
        instance.isActive = validated_data.get("isActive", instance.isActive)

        instance.save()
        return instance