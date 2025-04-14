# Generated by Django 5.1.1 on 2025-04-14 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_collegestudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollegeStudent',
        ),
        migrations.AddField(
            model_name='skills',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='CollegeStudent',
            fields=[
                ('student2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.student2')),
            ],
            bases=('home.student2',),
        ),
    ]
