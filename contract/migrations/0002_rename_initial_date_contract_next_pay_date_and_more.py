# Generated by Django 4.1.1 on 2022-10-23 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='initial_date',
            new_name='next_pay_date',
        ),
        migrations.AddField(
            model_name='contract',
            name='is_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='is_postpone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='pay_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='platforms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='platforms.platforms'),
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]