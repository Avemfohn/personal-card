# Generated by Django 4.1.2 on 2022-10-28 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0004_remove_personaleducation_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personelrow',
            name='personel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='personel.personel'),
        ),
    ]
