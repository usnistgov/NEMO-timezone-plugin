# Generated by Django 2.2.24 on 2021-10-13 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('NEMO', '0034_version_3_13_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferencesTimezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(blank=True, choices=[('US/Alaska', 'US/Alaska'), ('US/Arizona', 'US/Arizona'), ('US/Central', 'US/Central'), ('US/Eastern', 'US/Eastern'), ('US/Hawaii', 'US/Hawaii'), ('US/Mountain', 'US/Mountain'), ('US/Pacific', 'US/Pacific'), ('UTC', 'UTC')], help_text="Select the user's timezone", max_length=255, null=True)),
                ('user_preferences', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='timezone', to='NEMO.UserPreferences')),
            ],
            options={
                'verbose_name': 'Timezone',
                'verbose_name_plural': 'Timezone',
            },
        ),
        migrations.CreateModel(
            name='ToolTimezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(blank=True, choices=[('US/Alaska', 'US/Alaska'), ('US/Arizona', 'US/Arizona'), ('US/Central', 'US/Central'), ('US/Eastern', 'US/Eastern'), ('US/Hawaii', 'US/Hawaii'), ('US/Mountain', 'US/Mountain'), ('US/Pacific', 'US/Pacific'), ('UTC', 'UTC')], help_text="Select the tool's timezone", max_length=255, null=True)),
                ('tool', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='timezone', to='NEMO.Tool')),
            ],
            options={
                'verbose_name': 'Timezone',
                'verbose_name_plural': 'Timezone',
            },
        ),
    ]