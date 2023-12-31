# Generated by Django 4.2.4 on 2023-08-15 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_course_member_ship'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Lecture_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
