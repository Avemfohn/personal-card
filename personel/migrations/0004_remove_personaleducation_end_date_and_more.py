# Generated by Django 4.1.2 on 2022-10-28 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0003_remove_personaleducation_personel_personelrow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaleducation',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='personaleducation',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='personelrow',
            name='education',
        ),
        migrations.AddField(
            model_name='personelrow',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personelrow',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personel.personaleducation'),
        ),
        migrations.AddField(
            model_name='personelrow',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]