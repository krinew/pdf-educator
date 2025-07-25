# Generated by Django 5.2 on 2025-07-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(choices=[('CS101', 'Intro to Computer Science'), ('CS202', 'Data Structures')], default='CS101', help_text='Identifier for the course', max_length=10)),
                ('year', models.PositiveSmallIntegerField(help_text='Exam year of this past question')),
                ('question_type', models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('SUBJECTIVE', 'Subjective'), ('MISCELLANEOUS', 'Miscellaneous')], default='MCQ', help_text='Type of question (MCQ, Subjective, or Miscellaneous)', max_length=15)),
                ('text', models.TextField(help_text='The full question text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
