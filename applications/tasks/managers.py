from django.db import models
from django.db.models import Q


class TasksManager(models.Manager):

    def getActiveTasks(self):
        result = self.filter(
            Q(isActive=True)
        )
        return result
    
    def filterTasks(self, state):
        result = self.filter(
            Q(state__icontains=state) & Q(isActive=True)
        )
        return result
