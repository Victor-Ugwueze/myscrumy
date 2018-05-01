from django.db import models
from django.utils import timezone



class ScrumyUser(models.Model):
    SCRUMY_USER_ROLE = (
        ('O', 'Owner'),
        ('A', 'Admin'),
        ('Q', 'Quality Analyst'),
        ('D', 'Developer'),
    )
    username = models.CharField(max_length=150,null=False,unique=True)
    email = models.EmailField(max_length=150,null=False,unique=True)
    password = models.TextField(max_length=150,null=False,default='user@scrumyapp')
    role = models.CharField(choices=SCRUMY_USER_ROLE,default=1,max_length=1)

class GoalStatus(models.Model):
    GOAL_STATUS = (
        ('P', 'Pending'),
        ('V', 'Verified'),
        ('D', 'Done'),
         ('WG', 'Weekly Goal'),
        ('DT', 'Daily Task'),
    )
    status = models.CharField(max_length=1, choices=GOAL_STATUS)
    verified_by = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE,default=1)

class ScrumyGoals(models.Model):
    goal = models.CharField(max_length=150,null=False)
    user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    goal_status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE,default=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


