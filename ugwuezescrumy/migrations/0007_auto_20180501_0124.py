# Generated by Django 2.0.4 on 2018-05-01 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugwuezescrumy', '0006_goalstatus_verified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_status_id',
            field=models.ForeignKey(default='W', on_delete=django.db.models.deletion.CASCADE, to='ugwuezescrumy.GoalStatus'),
        ),
    ]
