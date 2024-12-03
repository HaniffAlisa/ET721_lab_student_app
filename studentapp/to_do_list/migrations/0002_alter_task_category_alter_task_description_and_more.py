# Generated by Django 5.1.3 on 2024-12-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("to_do_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="category",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
