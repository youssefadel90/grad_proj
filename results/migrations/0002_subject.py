# Generated by Django 4.0.3 on 2022-04-19 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0007_alter_lecture_video'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('semster', models.CharField(max_length=50)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.year')),
            ],
        ),
    ]