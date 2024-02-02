from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


#To Do Tasks
class Task(models.Model):
    name = models.CharField(verbose_name=_("Name"),max_length = 200,help_text=_("Name of the task."))
    important = models.BooleanField(verbose_name=_("Important"),default=False, help_text=_("Indicates if the task is important"))
    due_date = models.DateTimeField(verbose_name=_("Due Date"),help_text=("Date when a task is due"))
    time_spent = models.IntegerField(verbose_name=_("Complete"), help_text=_("Time spent on the task."), blank=True, null=True)
    complete = models.BooleanField(verbose_name=_("Complete"),default=False,help_text=_("Indicates if the task is complete."),)
    tags = models.ManyToManyField("Tag", blank=True,related_name="tasks",help_text=_("Tags or labels associated with the task."),verbose_name=_("Tags"),)
        

#Filters        
class Tag(models.Model):
    name = models.CharField(verbose_name=_("Name"),max_length = 100,help_text=_("Name of the tag."))
    is_mode = models.BooleanField(default=False,verbose_name=_("Is Mode"), help_text=_("Indicates if the tag is a mode."))

#Profiles
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField( blank=True)
    
    def __str__(self):
        return self.user.username

