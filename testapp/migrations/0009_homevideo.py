# Generated by Django 4.2.4 on 2023-10-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_alter_faq_options_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
