# Generated by Django 3.2.7 on 2021-09-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210911_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='house_feature',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_feature2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_feature3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_feature4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_feature5',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_image2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_image3',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_image4',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='house_image5',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
