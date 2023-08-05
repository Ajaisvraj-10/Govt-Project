# Generated by Django 4.1.6 on 2023-08-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_localvillage_panchayats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localvillage',
            name='panchayats',
        ),
        migrations.RemoveField(
            model_name='postoffice',
            name='revenue_village',
        ),
        migrations.RemoveField(
            model_name='revenuevillage',
            name='local_village',
        ),
        migrations.AddField(
            model_name='localvillage',
            name='revenue_village',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='localvillage_revenuevillage', to='locations.revenuevillage'),
        ),
        migrations.AddField(
            model_name='postoffice',
            name='local_village',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='postoffice_localvillage', to='locations.localvillage'),
        ),
        migrations.AddField(
            model_name='revenuevillage',
            name='panchayats',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revenuevillage_panchayats', to='locations.panchayats'),
        ),
    ]