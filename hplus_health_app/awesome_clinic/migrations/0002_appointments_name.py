# Generated by Django 4.0.5 on 2022-06-04 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awesome_clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='awesome_clinic.profile'),
        ),
    ]
