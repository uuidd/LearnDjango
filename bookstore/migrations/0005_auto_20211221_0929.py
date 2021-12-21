# Generated by Django 2.2.12 on 2021-12-21 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_book_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.CreateModel(
            name='AuthorWife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='名字')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Author')),
            ],
            options={
                'db_table': 'author_wife',
            },
        ),
    ]