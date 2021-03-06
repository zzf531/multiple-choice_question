# Generated by Django 3.0.5 on 2020-11-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=16, verbose_name='题目序号')),
                ('content', models.TextField(verbose_name='内容')),
                ('pic', models.CharField(max_length=100, verbose_name='图片')),
                ('options', models.TextField(verbose_name='选项')),
                ('answer', models.CharField(max_length=16, verbose_name='答案')),
                ('option_number', models.CharField(max_length=16, verbose_name='选项数')),
                ('reference', models.TextField(verbose_name='解释')),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
