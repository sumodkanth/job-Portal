# Generated by Django 5.0.2 on 2024-03-19 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0031_remove_jobstatus2_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminUI.studentdb')),
                ('newsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminUI.newsdb')),
            ],
        ),
    ]
