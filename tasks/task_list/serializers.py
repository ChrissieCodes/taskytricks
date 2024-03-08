from rest_framework import serializers
from task_list.models import Task, Tag, Profile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['name','important','due_date','complete','time_spent','start_date','created_date','recurrence_in_seconds','active']

        
        def create(self, validated_data):
            '''
            Create and return a task
            '''
            return Task.objects.create(**validated_data)
        
        def update(self, instance: Task , validated_data):
            """
            Update a task
            """
            return Task.objects.update(**validated_data)
            

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
        def create(self, validated_data):
            
            return Tag.objects.create(**validated_data)
        
        def update(self, instance:Tag, validated_data):
            
            return Tag.objects.update(**validated_data)
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        __field__ = '__all__'
        
        
        def create(self, validated_data):
            
            return Profile.objects.create(**validated_data)
        
        def update(self, instance:Tag, validated_data):
            
            return Profile.objects.update(**validated_data)