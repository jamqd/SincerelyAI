# Generated by Django 2.1.5 on 2019-01-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation',
            name='choice_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='equation',
            name='answer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equation',
            name='var1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equation',
            name='var2',
            field=models.IntegerField(default=0),
        ),
    ]