# Generated by Django 2.0.2 on 2018-03-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.DeleteModel(
            name='rest',
        ),
    ]