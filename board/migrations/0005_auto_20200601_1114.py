# Generated by Django 3.0.5 on 2020-06-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20200531_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='pdf',
            field=models.FileField(upload_to='files/pdfs/', verbose_name='File'),
        ),
    ]