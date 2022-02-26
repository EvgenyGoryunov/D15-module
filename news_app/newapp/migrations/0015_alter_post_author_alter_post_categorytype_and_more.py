# Generated by Django 4.0.1 on 2022-02-26 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0014_category_name_en_category_name_ru_post_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
    ]
