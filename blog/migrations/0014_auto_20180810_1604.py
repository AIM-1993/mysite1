# Generated by Django 2.0.7 on 2018-08-10 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_blog_read_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readnum',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]
