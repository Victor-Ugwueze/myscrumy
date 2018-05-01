from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ScrumyGoals,GoalStatus,ScrumyUser
from django.db import transaction

# Create your views here.


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    try:
        weekly_task = ScrumyGoals.objects.filter(goal_status_id=4)
        context = {'weekly_task':weekly_task}
        template = loader.get_template('task/index.html')
    except BaseException as e:
        raise e.message
    return HttpResponse(template.render(context,request))

  
    

def move_goal(request, task_id):
    try:
        scrummy_goal = ScrumyGoals.objects.filter(id=task_id)
        context = {'scrummy_goal': scrummy_goal}
        template = loader.get_template('task/detail.html')
    except BaseException as e:
        raise e.message
    return HttpResponse(template.render(context,request))


def add_user(request):
    try:
        user=ScrumyUser()
        user.username="emma"
        user.email="emma@gmail.com"
        user.password="gozman91"
        user.role=2
        user.save()
    except:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)

    scrumy_user_list=ScrumyUser.objects.all()
    users = ', '.join([eachuser.username for eachuser in scrumy_user_list])
    context = {'users': users}
    template = loader.get_template('task/add_user.html')
    return HttpResponse(template.render(context,request))
