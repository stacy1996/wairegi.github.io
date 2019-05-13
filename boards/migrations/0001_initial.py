# Generated by Django 2.1.7 on 2019-05-09 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('category', models.ForeignKey(null=True, on_delete='models.CASCADE', to='boards.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, null=True)),
                ('firstParticipant', models.CharField(max_length=255, null=True)),
                ('secondParticipant', models.CharField(max_length=255, null=True)),
                ('schoolName', models.CharField(max_length=255, null=True)),
                ('level', models.CharField(max_length=255, null=True)),
                ('teacherInChargeName', models.CharField(max_length=255, null=True)),
                ('teacherInChargePhone', models.CharField(max_length=255, null=True)),
                ('teacherInChargeEmail', models.EmailField(max_length=255, null=True)),
                ('principalName', models.CharField(max_length=255, null=True)),
                ('principalPhone', models.CharField(max_length=255, null=True)),
                ('principalEmail', models.EmailField(max_length=255, null=True)),
                ('intro', models.TextField()),
                ('aims', models.TextField()),
                ('proposal', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('category', models.ForeignKey(null=True, on_delete='models.CASCADE', related_name='projects', to='boards.Category')),
                ('user', models.ForeignKey(null=True, on_delete='models.CASCADE', related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(null=True, on_delete='models.CASCADE', related_name='posts', to='boards.Project'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
