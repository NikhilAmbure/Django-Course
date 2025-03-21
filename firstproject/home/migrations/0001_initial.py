# Generated by Django 5.1.1 on 2024-10-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('female', 'female')], default='Male', max_length=10)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='student')),
                ('file', models.FileField(upload_to='files')),
                ('student_bio', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
