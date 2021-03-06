# Generated by Django 3.1.2 on 2020-11-02 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания')),
                ('content', models.FileField(upload_to='')),
                ('content_type', models.CharField(choices=[('ODH_DATA', 'Odh Data'), ('XlS_DATA', 'Xls Data')], default='XlS_DATA', max_length=8)),
            ],
        ),
    ]
