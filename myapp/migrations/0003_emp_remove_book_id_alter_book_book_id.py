# Generated by Django 5.1.1 on 2024-10-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
