# Generated by Django 3.1.1 on 2021-05-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=120)),
                ('Subject', models.TextField(max_length=1200)),
                ('Massage', models.DateField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
