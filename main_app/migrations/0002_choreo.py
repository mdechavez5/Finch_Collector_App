# Generated by Django 4.0.4 on 2022-06-01 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choreo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('vid', models.CharField(max_length=250)),
                ('embed', models.CharField(max_length=300)),
                ('dancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choreo', to='main_app.dancer')),
            ],
        ),
    ]
