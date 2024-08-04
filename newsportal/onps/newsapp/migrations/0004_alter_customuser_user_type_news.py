# Generated by Django 5.0.6 on 2024-06-04 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'subadmin')], default=1, max_length=50),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitle', models.TextField(blank=True)),
                ('postdetails', models.TextField(blank=True)),
                ('status', models.CharField(max_length=50)),
                ('postimage', models.ImageField(upload_to='media/news')),
                ('postedby', models.CharField(max_length=50)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=50)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.category')),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.subcategory')),
            ],
        ),
    ]
