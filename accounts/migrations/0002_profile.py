# Generated by Django 4.2.4 on 2023-08-12 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('coin', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/users')),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
