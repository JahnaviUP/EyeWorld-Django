# Generated by Django 3.0.8 on 2021-03-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_faceshape'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shape',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
