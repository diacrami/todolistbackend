from django.db import models
from .managers import TasksManager

# Create your models here.
class Tasks(models.Model):

    STATE_CHOICES = (
        ('C', 'Completed'),
        ('T', 'To Do')
    )

    taskid = models.AutoField(primary_key=True)
    taskname = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='T')
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True);
    updatedAt = models.DateTimeField(auto_now=True);

    objects = TasksManager()

    def complete_info(self):
        return "{}".format(self.taskid,self.taskname,self.state,self.isActive)
    
    def __str__(self):
        return self.complete_info()
    
    class Meta:
        db_table = 'tasks'