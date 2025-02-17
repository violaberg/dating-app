from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_age_preference_profile_gender_preference_and_more'),
        ('questionnaire', '0002_seed_initial_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='Profile',
            name='gender_preferences',
            field=models.ManyToManyField(blank=True, related_name='profiles_gender_preference', to='questionnaire.choice'),
        ),
        migrations.AddField(
            model_name='Profile',
            name='age_preferences',
            field=models.ManyToManyField(blank=True, related_name='profiles_age_preference', to='questionnaire.choice'),
        ),
        migrations.AddField(
            model_name='Profile',
            name='spark_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles_spark_type', to='questionnaire.choice'),
        ),
    ]
