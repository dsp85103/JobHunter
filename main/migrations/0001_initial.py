# Generated by Django 2.2.1 on 2019-06-11 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrepreneur_content',
            fields=[
                ('entrepreneur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('companytitle', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postid', models.IntegerField(primary_key=True, serialize=False)),
                ('jobtype', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('condition', models.TextField()),
                ('benefit', models.TextField()),
                ('contact', models.TextField()),
                ('min_salary', models.PositiveIntegerField()),
                ('viewed', models.IntegerField()),
                ('like', models.IntegerField()),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_content',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('resume', models.TextField()),
                ('mis_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ViewList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Post')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('qaid', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Entrepreneur_content')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Post')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student_content')),
            ],
        ),
        migrations.CreateModel(
            name='LikeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Post')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
